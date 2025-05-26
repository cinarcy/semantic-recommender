import pandas as pd
import faiss
import os
from sentence_transformers import SentenceTransformer
import numpy as np

ARTICLES_PATH = "recommender/articles.csv"
INDEX_DIR = "index"
INDEX_PATH = os.path.join(INDEX_DIR, "faiss_index.bin")
MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

def generate_embeddings(texts, model_name=MODEL_NAME):
    model = SentenceTransformer(model_name)
    return model.encode(texts, show_progress_bar=True)

def build_and_save_index():
    if not os.path.exists(ARTICLES_PATH):
        raise FileNotFoundError(f"Dataset not found at {ARTICLES_PATH}")

    df = pd.read_csv(ARTICLES_PATH)
    texts = (df["title"] + ". " + df["description"]).tolist()
    embeddings = generate_embeddings(texts)

    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings).astype("float32"))

    os.makedirs(INDEX_DIR, exist_ok=True)
    faiss.write_index(index, INDEX_PATH)

    df.to_csv(os.path.join(INDEX_DIR, "articles.csv"), index=False)
    print(f"Index and metadata saved to '{INDEX_DIR}/'.")

if __name__ == "__main__":
    build_and_save_index()
