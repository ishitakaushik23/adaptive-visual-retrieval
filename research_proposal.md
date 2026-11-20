# Region-Level Feedback-Adaptive Multimodal Retrieval

**Author:** Ishita Kaushik, IIT Jammu (B.Tech Mathematics & Computing)

## 1. Problem Statement

Vision-language retrieval systems such as CLIP represent each image with one global embedding. On cluttered, multi-object images this vector blends every object together, so a query about one object matches poorly. Relevance feedback has a related weakness: when a user marks a whole image as relevant or irrelevant, the system cannot tell which object in the image the user meant.

## 2. Prior Work

Levi et al., *Object-Centric Open-Vocabulary Image-Retrieval with Aggregated Features* (BMVC 2023), observe that one global embedding per image limits retrieval of small object instances. They propose **Dense-CLIP**, which uses CLIP's local features, and **Cluster-CLIP**, which clusters those local features and keeps the cluster centroids so the index stays small. Their setting is static, one-shot text-to-image retrieval.

## 3. Version 1 (baseline)

Whole-image retrieval with OpenCLIP ViT-B/32 (zero-shot): one embedding per image, cosine-similarity top-k, no feedback, no metric.

## 4. What This Work Adds

| | Prior work | This work |
|---|---|---|
| Object-level granularity | CLIP local features + clustering | YOLOv8 detected regions, each embedded with CLIP |
| Interaction | None (static retrieval) | Multi-round relevance feedback (Rocchio-style query update) |
| Queries | Text | Text and image (shared CLIP space) |
| Question asked | Does object-level help retrieval? | Does object-level help feedback *converge faster*, especially on cluttered images? |

**Research question.** Does decomposing images into object regions let relevance feedback converge faster than whole-image feedback on cluttered, multi-object images?

**Hypothesis.** Region-level feedback converges faster on cluttered images. On simple single-subject images the two should be similar, since there is little to disentangle.

## 5. Method

1. Detect object regions per image with YOLOv8 (fallback: whole image if nothing is detected).
2. Embed whole images and each region with CLIP.
3. Score an image by its best-matching region (max over regions).
4. After each round, update the query with Rocchio: move toward relevant items, away from irrelevant ones.
5. Four-condition ablation: whole-image / region-level, each with and without feedback.

## 6. Evaluation Setup

- Data: COCO128 (128 images), split by YOLO-detected object count into simple (fewest objects) and cluttered (most objects) subsets.
- Queries: 15 text queries per subset, one labeled relevant image each (`data/queries_simple.json`, `data/queries_cluttered.json`).
- Feedback is simulated from the ground-truth labels. 5 rounds, top-5 results.
- Metric: MRR. Recall@k was tried first and could not show the effect, because with one relevant image per query it only takes the values 0 or 1/k regardless of rank position.

## 7. Results

*Replace the table below with `results_table.csv` (produced by the notebook).*

| Set | Condition | MRR round 0 | MRR round 1 | MRR final | 95% CI (final) |
|---|---|---|---|---|---|
| simple | whole_baseline | | | | |
| simple | whole_feedback | | | | |
| simple | region_baseline | | | | |
| simple | region_feedback | | | | |
| cluttered | whole_baseline | | | | |
| cluttered | whole_feedback | | | | |
| cluttered | region_baseline | | | | |
| cluttered | region_feedback | | | | |

Per-query comparison, region_feedback vs whole_feedback at the final round (wins / ties / losses): simple = _ / _ / _, cluttered = _ / _ / _.

*Preliminary run (earlier query set, to be superseded by the table above):* on cluttered images region-level feedback reached MRR 0.2 by round 1, while whole-image feedback climbed gradually to 0.083 by round 4. On simple images both ended near 0.133.

**Reading the baselines.** `whole_baseline` to `region_baseline` isolates what object-level decomposition adds on its own (the idea in the prior work). `region_baseline` to `region_feedback` isolates what feedback adds on top (this work's extension).

## 8. Why It Is Useful

Interactive search over cluttered image collections (product catalogs, photo libraries, visual discovery feeds) where users refine results by marking a few as good or bad. Region-level feedback gives that signal a precise object to attach to.

## 9. Limitations

- Feedback is simulated, not collected from real users.
- One relevant image per query makes scores coarse; n = 15 per subset gives wide confidence intervals.
- COCO128 is small, and YOLOv8 only detects COCO's 80 classes.
- The prior method was not reimplemented. `region_baseline` stands in for the object-centric idea.

## 10. Future Work

- Larger labeled query sets (about 50 per subset) and the full COCO validation set.
- Mean vs. max aggregation across regions.
- Compare against CLIP local-feature / clustering-based object embeddings.
- Other vision-language backbones.