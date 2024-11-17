from app.utils.logger import setup_logger
from app.models.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain_community.llms import Ollama
from app.config.settings import Config
from typing import Dict, Any, Optional, Tuple
from datetime import datetime

logger = setup_logger(__name__)

class DocumentAnalyzer:
    def __init__(self, embed_folder: str):
        self.embed_folder = embed_folder
        self.embedding_function = OllamaEmbeddings()
        self.llm = Ollama(model=Config.LLM_MODEL)

    def analyze(self, query: str) -> Tuple[bool, Optional[Dict[str, Any]], Optional[str]]:
        """
        Analyze a document using LLM.
        
        Returns:
            Tuple[bool, Optional[Dict], Optional[str]]: (success, result, error_message)
        """
        try:
            vector_store = Chroma(
                persist_directory=self.embed_folder,
                embedding_function=self.embedding_function
            )
            
            retriever = vector_store.as_retriever(search_kwargs={"k": 3})
            
            qa_chain = RetrievalQA.from_chain_type(
                llm=self.llm,
                chain_type="stuff",
                retriever=retriever,
                return_source_documents=True
            )

            result = qa_chain({"query": query})
            
            response = {
                "analysis": result['result'],
                "metadata": {
                    "model_used": Config.LLM_MODEL,
                    "timestamp": datetime.now().isoformat()
                }
            }
            
            return True, response, None
            
        except Exception as e:
            error_msg = f"Error analyzing document: {str(e)}"
            logger.error(error_msg)
            return False, None, error_msg 