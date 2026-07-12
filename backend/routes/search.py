from fastapi import APIRouter

from backend.models.schemas import SearchRequest, SearchResponse, ChunkResult
from backend.services.embeddings import embed_texts
from backend.services.vector_store import search as vector_search

router = APIRouter(prefix="/search", tags=["search"])


@router.post("", response_model=SearchResponse)
async def search_chunks(request: SearchRequest):
    query_vector = embed_texts([request.query])[0]
    hits = vector_search(query_vector, top_k=request.top_k)

    results = [
        ChunkResult(
            document_id=hit.payload["document_id"],
            title=hit.payload["title"],
            page=hit.payload["page"],
            chunk_number=hit.payload["chunk_number"],
            content=hit.payload["content"],
            score=hit.score,
        )
        for hit in hits
    ]

    return SearchResponse(query=request.query, results=results)