import os
import shutil
import tempfile
import uuid

from fastapi import APIRouter, UploadFile, File, HTTPException

from backend.models.schemas import UploadResponse
from backend.services.pdf_extractor import extract_text_by_page
from backend.services.chunker import chunk_text
from backend.services.embeddings import embed_texts
from backend.services.vector_store import upsert_chunks

router = APIRouter(prefix="/documents", tags=["documents"])


@router.post("/upload", response_model=UploadResponse)
async def upload_document(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported in this PR")

    document_id = str(uuid.uuid4())

    # Save the upload to a temp file so pypdf can read it
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        shutil.copyfileobj(file.file, tmp)
        tmp_path = tmp.name

    try:
        pages = extract_text_by_page(tmp_path)
        if not pages:
            raise HTTPException(status_code=422, detail="No extractable text found in PDF")

        all_vectors = []
        all_payloads = []
        chunk_counter = 0

        for page_number, page_text in pages:
            chunks = chunk_text(page_text)
            if not chunks:
                continue
            vectors = embed_texts(chunks)
            for chunk_content, vector in zip(chunks, vectors):
                chunk_counter += 1
                all_vectors.append(vector)
                all_payloads.append({
                    "document_id": document_id,
                    "title": file.filename,
                    "page": page_number,
                    "chunk_number": chunk_counter,
                    "content": chunk_content,
                })

        if all_vectors:
            upsert_chunks(all_vectors, all_payloads)

        return UploadResponse(
            document_id=document_id,
            title=file.filename,
            pages_processed=len(pages),
            chunks_created=chunk_counter,
        )
    finally:
        os.remove(tmp_path)