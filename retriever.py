"""
Simple RAG retrieval using TF-IDF similarity.
No external vector DB or embedding API needed.
"""

import re
import math
from collections import Counter
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from knowledge_base import KNOWLEDGE_CHUNKS


def tokenize(text: str) -> list[str]:
    """Simple tokenizer: lowercase, split on non-alphanumeric."""
    return re.findall(r'[a-z0-9çğıöşü]+', text.lower())


def compute_idf(documents: list[list[str]]) -> dict[str, float]:
    """Compute inverse document frequency for all terms."""
    n = len(documents)
    df = Counter()
    for doc in documents:
        unique_terms = set(doc)
        for term in unique_terms:
            df[term] += 1
    return {term: math.log(n / freq) for term, freq in df.items()}


def tfidf_vector(tokens: list[str], idf: dict[str, float]) -> dict[str, float]:
    """Create a TF-IDF vector for a token list."""
    tf = Counter(tokens)
    max_tf = max(tf.values()) if tf else 1
    return {term: (count / max_tf) * idf.get(term, 0) for term, count in tf.items()}


def cosine_similarity(v1: dict[str, float], v2: dict[str, float]) -> float:
    """Cosine similarity between two sparse vectors."""
    common = set(v1) & set(v2)
    dot = sum(v1[t] * v2[t] for t in common)
    mag1 = math.sqrt(sum(x ** 2 for x in v1.values()))
    mag2 = math.sqrt(sum(x ** 2 for x in v2.values()))
    if mag1 == 0 or mag2 == 0:
        return 0.0
    return dot / (mag1 * mag2)


class Retriever:
    def __init__(self):
        self.chunks = KNOWLEDGE_CHUNKS
        self.doc_tokens = []
        for chunk in self.chunks:
            text = chunk["topic"] + " " + chunk["content"]
            self.doc_tokens.append(tokenize(text))
        self.idf = compute_idf(self.doc_tokens)
        self.doc_vectors = [tfidf_vector(tokens, self.idf) for tokens in self.doc_tokens]

    def retrieve(self, query: str, top_k: int = 5) -> list[dict]:
        """Retrieve top_k most relevant chunks for a query."""
        query_tokens = tokenize(query)
        query_vec = tfidf_vector(query_tokens, self.idf)

        scored = []
        for i, doc_vec in enumerate(self.doc_vectors):
            sim = cosine_similarity(query_vec, doc_vec)
            scored.append((sim, i))

        scored.sort(reverse=True)
        results = []
        for sim, idx in scored[:top_k]:
            if sim > 0.0:
                results.append({
                    "topic": self.chunks[idx]["topic"],
                    "content": self.chunks[idx]["content"],
                    "score": round(sim, 4)
                })
        return results


# Singleton
_retriever = None

def get_retriever() -> Retriever:
    global _retriever
    if _retriever is None:
        _retriever = Retriever()
    return _retriever
