---
name: chunking-strategy-guide
description: "Methodology for systematically designing document chunking strategies for RAG pipelines. Use this skill for 'chunking strategy', 'document splitting', 'RAG chunking', 'embedding optimisation', 'semantic chunking', 'text splitting', and other RAG data preprocessing tasks. Note: vector DB infrastructure construction and embedding model training are outside the scope of this skill."
---

# Chunking Strategy Guide — RAG Document Chunking Strategy

A skill that enhances the data preprocessing capabilities of the rag-architect.

## Target Agents

- **rag-architect** — Effectively chunks documents to improve retrieval quality
- **eval-specialist** — Evaluates the retrieval quality of chunking strategies

## Chunking Strategy Comparison

| Strategy | Principle | Advantages | Disadvantages | Best For |
|----------|----------|-----------|--------------|---------|
| Fixed-size | Cut at N-token intervals | Simple implementation | Semantic breaks | Logs, code |
| Sentence-based | Split by sentence | Preserves meaning | Uneven sizes | News, blogs |
| Paragraph-based | Split at blank lines | Maintains logical units | Paragraph size variance | Documents, reports |
| Semantic | Based on embedding similarity | Highest quality | Slow, costly | Complex documents |
| Recursive | Hierarchical separators | Balanced | Complex configuration | General-purpose |
| Markdown | Based on headings | Preserves structure | MD-only | Technical docs |

## Chunking Parameter Guide

### Optimal Chunk Sizes

```
| Document Type | Chunk Size | Overlap | Rationale |
|--------------|-----------|---------|-----------|
| FAQ | 100-200 tokens | 0 | Q&A pairs are short |
| Technical docs | 300-500 tokens | 50 | Code + explanation units |
| Legal documents | 500-800 tokens | 100 | Article units |
| Academic papers | 400-600 tokens | 80 | Paragraph units |
| Chat logs | 200-300 tokens | 30 | Conversation turn units |
| Fiction/essays | 300-500 tokens | 50 | Scene/paragraph units |
```

### Overlap Ratio Formula

```
optimal_overlap = chunk_size * 0.1 to 0.2

Rules:
- Independent documents (FAQ): Overlap 0
- Sequential documents (manuals): 10-15%
- Dense documents (legal): 15-20%
- Maximum overlap: Never exceed 25% of chunk_size
```

## Semantic Chunking Algorithm

```python
def semantic_chunking(text, model, threshold=0.5):
    """
    1. Split into sentences
    2. Calculate cosine similarity of adjacent sentence embeddings
    3. Split at points where similarity falls below threshold
    4. Apply min/max chunk size constraints
    """
    sentences = split_sentences(text)
    embeddings = model.encode(sentences)

    breakpoints = []
    for i in range(len(embeddings) - 1):
        sim = cosine_similarity(embeddings[i], embeddings[i+1])
        if sim < threshold:
            breakpoints.append(i + 1)

    chunks = split_at(sentences, breakpoints)
    return enforce_size_limits(chunks, min=100, max=800)
```

## Per-Document-Type Preprocessing Pipeline

### PDF

```
PDF > Text extraction (pdfplumber/pymupdf)
> Remove headers/footers
> Remove page numbers
> Tables > Markdown conversion
> Images > alt text / OCR
> Metadata extraction (title, author, date)
> Chunking
```

### HTML/Webpages

```
HTML > Body extraction (trafilatura/readability)
> Remove navigation/sidebar/ads
> Markdown conversion
> Preserve link text ([text](URL))
> Preserve tables
> Metadata extraction (title, description)
> Chunking
```

### Code

```
Code > AST parsing
> Split by function/class
> Docstring + signature + body
> Add file path metadata
> Link related test code
> Chunking (function-level)
```

## Metadata Enrichment Strategy

```python
chunk_with_metadata = {
    "text": "Chunk text...",
    "metadata": {
        "source": "document.pdf",
        "page": 5,
        "section": "3.2 Architecture",
        "heading_hierarchy": ["3. Design", "3.2 Architecture"],
        "chunk_index": 12,
        "total_chunks": 45,
        "created_at": "2025-01-15",
        "document_type": "technical_spec",
        "language": "en"
    }
}
```

## Chunking Quality Evaluation Metrics

| Metric | Formula | Threshold |
|--------|---------|-----------|
| Information completeness | Original key info / total key info | >= 95% |
| Semantic break rate | Mid-sentence cuts / total chunks | <= 5% |
| Size uniformity | 1 - (std / mean) | >= 0.7 |
| Retrieval precision | Relevant chunks / returned chunks (top-5) | >= 60% |
| Retrieval recall | Returned relevant / total relevant (top-10) | >= 80% |

## Embedding Model Selection Guide

| Model | Dimensions | Multilingual | Cost | Use Case |
|-------|-----------|-------------|------|---------|
| text-embedding-3-small | 1536 | Good | $0.02/1M | General-purpose, cost-efficient |
| text-embedding-3-large | 3072 | Good | $0.13/1M | High quality |
| multilingual-e5-large | 1024 | Excellent | Free (local) | Multilingual specialisation |
| bge-m3 | 1024 | Excellent | Free (local) | Multilingual, long context |
| voyage-multilingual-2 | 1024 | Excellent | $0.12/1M | Best multilingual |
