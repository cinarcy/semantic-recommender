from pydantic import BaseModel
from typing import List

class Article(BaseModel):
    title: str
    description: str
    category: str

class RecommendationResponse(BaseModel):
    query: str
    results: List[Article]
