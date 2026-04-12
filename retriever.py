# retriever module
# uses tf-idf with bigrams to find the most relevant chunks for a given query
# no need for an external vector db since the dataset is small enough

import re
import math
from collections import Counter
from knowledge_base import KNOWLEDGE_CHUNKS


def tokenize(text):
    # lowercase everything and merge terms like "ie 300" into "ie300"
    text = text.lower()
    text = re.sub(r'\bie[\s\-_]*(\d{3})', r'ie\1', text)
    text = re.sub(r'\bq[\s]*(\d)', r'q\1', text)
    tokens = re.findall(r'[a-z0-9çğıöşü]+', text)
    return tokens


def make_bigrams(tokens):
    # combine consecutive words into pairs for better matching
    bigrams = []
    for i in range(len(tokens) - 1):
        bigrams.append(tokens[i] + "_" + tokens[i + 1])
    return bigrams


def compute_idf(documents):
    # inverse document frequency - words that appear in fewer docs get higher weight
    n = len(documents)
    df = Counter()
    for doc in documents:
        for term in set(doc):
            df[term] += 1
    return {term: math.log(n / freq) for term, freq in df.items()}


def tfidf_vector(tokens, idf):
    # build a tf-idf vector from tokens
    tf = Counter(tokens)
    max_tf = max(tf.values()) if tf else 1
    return {term: (count / max_tf) * idf.get(term, 0) for term, count in tf.items()}


def cosine_similarity(v1, v2):
    # standard cosine similarity between two sparse vectors
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

        # tokenize each chunk (topic + content) and also get bigrams
        self.doc_tokens = []
        for chunk in self.chunks:
            text = chunk["topic"] + " " + chunk["content"]
            unigrams = tokenize(text)
            bigrams = make_bigrams(unigrams)
            self.doc_tokens.append(unigrams + bigrams)

        # precompute idf and document vectors so we dont redo it every query
        self.idf = compute_idf(self.doc_tokens)
        self.doc_vectors = [tfidf_vector(tokens, self.idf) for tokens in self.doc_tokens]

    def retrieve(self, query, top_k=5):
        # tokenize the query the same way
        q_unigrams = tokenize(query)
        q_bigrams = make_bigrams(q_unigrams)
        query_tokens = q_unigrams + q_bigrams
        query_vec = tfidf_vector(query_tokens, self.idf)

        # score each chunk against the query
        scored = []
        for i, doc_vec in enumerate(self.doc_vectors):
            sim = cosine_similarity(query_vec, doc_vec)
            scored.append((sim, i))

        scored.sort(reverse=True)

        # return top_k results that have some similarity
        results = []
        for sim, idx in scored[:top_k]:
            if sim > 0.0:
                results.append({
                    "topic": self.chunks[idx]["topic"],
                    "content": self.chunks[idx]["content"],
                    "score": round(sim, 4)
                })
        return results


# keep a single instance so we dont rebuild the index every time
_retriever = None

def get_retriever():
    global _retriever
    if _retriever is None:
        _retriever = Retriever()
    return _retriever
