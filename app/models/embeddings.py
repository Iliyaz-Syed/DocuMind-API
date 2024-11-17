from langchain_community.embeddings import OllamaEmbeddings as BaseOllamaEmbeddings
from typing import List
from app.utils.logger import setup_logger
from app.config.settings import Config

logger = setup_logger(__name__)

class OllamaEmbeddings(BaseOllamaEmbeddings):
    """Custom Ollama embeddings class with additional functionality."""
    
    def __init__(self):
        super().__init__(
            model=Config.LLM_MODEL,
            base_url=Config.LLM_BASE_URL
        )

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """Generate embeddings for a list of documents."""
        try:
            embeddings = super().embed_documents(texts)
            logger.debug(f"Generated embeddings for {len(texts)} documents")
            return embeddings
        except Exception as e:
            logger.error(f"Error generating embeddings: {str(e)}")
            raise

    def embed_query(self, text: str) -> List[float]:
        """Generate embeddings for a query string."""
        try:
            embedding = super().embed_query(text)
            logger.debug("Generated embedding for query")
            return embedding
        except Exception as e:
            logger.error(f"Error generating query embedding: {str(e)}")
            raise 