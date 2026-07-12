from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Qdrant
    qdrant_host: str = "localhost"
    qdrant_port: int = 6333
    qdrant_collection_name: str = "ekip_chunks"

    # Embeddings
    embedding_model_name: str = "all-MiniLM-L6-v2"   # 384-dim, small & fast, no API key
    embedding_dimension: int = 384

    # Chunking
    chunk_size: int = 500       # characters per chunk
    chunk_overlap: int = 50     # characters of overlap between consecutive chunks

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()