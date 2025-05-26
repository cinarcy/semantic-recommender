from fastapi import FastAPI, Query
from app.model import load_index, search_similar_articles
from app.schemas import RecommendationResponse
from typing import List

app = FastAPI(title="Semantic Recommender")

index, articles = load_index()

@app.get("/recommend", response_model=RecommendationResponse)
def recommend(q: str = Query(..., description="Input query text"), k: int = 5):
    results = search_similar_articles(index, articles, q, k)
    return {"query": q, "results": results}
