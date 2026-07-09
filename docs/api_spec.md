# API Specification (Planned)

> Status: **Planning only** — no endpoints are implemented yet in PR #1.
> This document exists so the contract is agreed on before PR #2 (Basic RAG) starts building it.
> Update this file in the PR that implements each endpoint.

## Auth

### `POST /auth/login`
Authenticate a user and return a session/JWT token.

## Documents

### `POST /documents/upload`
Upload a document (PDF, API spec, technical doc, or Markdown file) for ingestion.

### `GET /documents`
List uploaded documents with metadata (title, source_type, uploaded_by, upload_timestamp).

### `DELETE /documents/{id}`
Remove a document and its associated chunks/embeddings.

## Search

### `POST /search`
Run a hybrid (vector + keyword) search over ingested chunks and return top-N ranked results.

## Chat

### `POST /chat`
Ask a natural-language question. Returns a generated answer with citations
(source document, page number, chunk reference, confidence score) and maintains
conversational context via `conversation_id`.

---

Each endpoint above will get full request/response schemas, status codes, and auth
requirements added as it's implemented (starting PR #2).
