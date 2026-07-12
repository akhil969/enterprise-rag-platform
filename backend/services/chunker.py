from typing import List
from backend.config import settings


def chunk_text(text: str, chunk_size: int = None, overlap: int = None) -> List[str]:
    """
    Simple character-based sliding-window chunker.
    Overlap keeps context from getting cut off mid-idea at chunk boundaries.
    """
    chunk_size = chunk_size or settings.chunk_size
    overlap = overlap or settings.chunk_overlap

    text = text.strip()
    if not text:
        return []

    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap  # step forward, re-including the overlap window

    return chunks