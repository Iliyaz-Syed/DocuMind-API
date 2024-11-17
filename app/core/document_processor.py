from app.utils.logger import setup_logger
from app.models.embeddings import OllamaEmbeddings
from app.utils.file_handlers import extract_text_from_file
from langchain_community.vectorstores import Chroma
from langchain.schema import Document
from typing import Optional, Tuple
import os

logger = setup_logger(__name__)

class DocumentProcessor:
    def __init__(self, embed_folder: str):
        self.embed_folder = embed_folder
        self.embedding_function = OllamaEmbeddings()

    def process_document(self, file_path: str) -> Tuple[bool, Optional[str]]:
        """
        Process a document and generate embeddings.
        
        Returns:
            Tuple[bool, Optional[str]]: (success, error_message)
        """
        try:
            # Extract text using the appropriate method
            text = extract_text_from_file(file_path)
            
            # Create documents with metadata
            documents = [Document(
                page_content=text,
                metadata={"source": file_path}
            )]
            
            # Create and persist embeddings
            Chroma.from_documents(
                documents=documents,
                embedding=self.embedding_function,
                persist_directory=self.embed_folder
            )
            
            return True, None
        except Exception as e:
            error_msg = f"Error processing document: {str(e)}"
            logger.error(error_msg)
            return False, error_msg 