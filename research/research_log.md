# Experiment 1 (July 6, 2026)

## Goal
Build a semantic retrieval baseline using CLIP.

## Model
CLIP ViT-B/32

## Dataset
Fashion Product Dataset

## Method
Cosine similarity

## Results
- Top-5 retrieval works well.
- Similar clothing categories are retrieved.

## Limitations
- Linear search
- No personalization
- No quantitative evaluation

## observation
Query 10 - retrieved all shoes - colour first then pattern 
qyery 35 - all shirts - went by pattern and colour
query 82 - all slippers - went by pattern and similar style
query 145(brown leather bag) - all leather bags + normal bags - colour and leather bags were first
query 201(full sleeve mens tshirt) - all mens tshirts - went by print of tshirt and fitting of tshirt first

## Next Step
Implement FAISS indexing.

# Experiment 2 (July 7, 2026)

## Goal
Replace brute-force retrieval with FAISS indexing.

## Observation
- FAISS returned identical Top-5 retrieval results.
- Retrieval quality remained unchanged.
- FAISS replaces linear similarity search with an optimized vector index.
- This approach is expected to scale much better for larger datasets.

## Conclusion
The retrieval pipeline is now more scalable without affecting semantic retrieval quality.


# Experiment 3

Goal:
Benchmark brute force vs FAISS.

Results:

Brute Force:
4.0s
Brute Force Average Time: 0.039688 seconds

FAISS:
3.8s

Conclusion:

At small dataset sizes, both methods perform similarly.

However, FAISS is designed for large-scale vector retrieval.

# Experiment 3 (July 7, 2026)

## Question
Does FAISS become more useful as the embedding database grows?

## What I tried
- Expanded the embedding matrix using `np.tile()`.
- Built a larger FAISS index.
- Benchmarked brute-force search and FAISS separately.
- Measured only the retrieval stage (excluding CLIP inference).

## Results
- FAISS and brute-force produced identical retrieval results.
- For the original dataset (~500 embeddings), the timing difference was very small.
- Large-scale benchmarking could not be completed because the local machine repeatedly crashed during testing.

## What I learned
- Search benchmarking should isolate retrieval from embedding generation.
- `np.tile()` can simulate larger vector databases for experiments.
- Local hardware can become the limiting factor during scalability testing.

## Next Step
Move from optimizing retrieval speed to improving retrieval quality through adaptive retrieval.

why did i do this?
establishes scalable baseline