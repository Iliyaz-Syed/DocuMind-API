import os
from pathlib import Path

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Flask Configuration
class Config:
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
    EMBED_FOLDER = os.path.join(BASE_DIR, 'embeddings')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'docx'}
    
    # LLM Configuration
    LLM_MODEL = "llama3.2:latest"
    LLM_BASE_URL = os.getenv('LLM_BASE_URL', 'http://localhost:11434/v1')
    
    # Create necessary directories
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    os.makedirs(EMBED_FOLDER, exist_ok=True) 