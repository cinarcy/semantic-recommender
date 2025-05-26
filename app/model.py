import os
import pandas as pd
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

INDEX_PATH = "index/faiss_index.bin"
ARTICLES_PATH = "index/articles.csv"
MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

def load_index():
    if not os.path.exists(INDEX_PATH):
        raise FileNotFoundError("FAISS index not found. Please run build_index.py first.")
    index = faiss.read_index(INDEX_PATH)
    articles = pd.read_csv(ARTICLES_PATH)
    return index, articles

def search_similar_articles(index, articles_df, query, k=5):
    model = SentenceTransformer(MODEL_NAME)
    query_embedding = model.encode([query])[0].astype("float32")
    distances, indices = index.search(np.array([query_embedding]), k)
    results = []
    for idx in indices[0]:
        article = articles_df.iloc[idx]
        results.append({
            "title": article["title"],
            "description": article["description"],
            "category": article["category"]
        })
    return results
