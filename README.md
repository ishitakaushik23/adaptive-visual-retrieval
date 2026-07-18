# Adaptive Visual Retrieval

A research project on feedback-adaptive, region-level multimodal image
retrieval — investigating whether decomposing images into detected object
regions improves how quickly interactive relevance feedback converges to a
user's intended result, particularly on cluttered, multi-object scenes.

See `research_proposal.md` for the full research question, hypothesis, and
evaluation design.

## Status

- **v1** (`notebooks/retrieval_v1.ipynb`): whole-image CLIP (OpenCLIP
  ViT-B/32) retrieval baseline. Zero-shot embeddings, cosine-similarity
  top-k over a 500-image collection. No adaptivity, no multimodal query
  support, no evaluation metrics.
- **v2** (`notebooks/retrieval_v2.ipynb`, in progress): adds YOLOv8-based
  region detection, multimodal (text + image) queries via CLIP's shared
  embedding space, and Rocchio-style feedback-adaptive re-ranking — run as a
  four-condition ablation (whole-image vs. region-level, with vs. without
  feedback) rather than a single end-to-end system. See `dataset.md` for the
  labeled query set spec this depends on.

## Repo structure

```
notebooks/
  retrieval_v1.ipynb    # v1 whole-image baseline
  retrieval_v2.ipynb    # v2 scaffold — ablation structure, implementation in progress
data/
  queries_simple.json      # TODO: labeled queries, single-subject images
  queries_cluttered.json   # TODO: labeled queries, multi-object images
research_proposal.md   # research question, hypothesis, evaluation design
dataset.md             # base image collection + labeled query set spec
```

## Setup


pip install open_clip_torch ultralytics matplotlib scikit-learn


## Next steps

See the "Notes / next steps" section at the end of `retrieval_v2.ipynb`.
