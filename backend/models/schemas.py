from pydantic import BaseModel
from typing import List


class UploadResponse(BaseModel):
    document_id: str
    title: str
    pages_processed: int
    chunks_created: int


class SearchRequest(BaseModel):
    query: str
    top_k: int = 5


class ChunkResult(BaseModel):
    document_id: str
    title: str
    page: int
    chunk_number: int
    content: str
    score: float


class SearchResponse(BaseModel):
    query: str
    results: List[ChunkResult]