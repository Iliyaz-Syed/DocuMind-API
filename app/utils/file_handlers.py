from app.utils.logger import setup_logger
from app.config.settings import Config
import os
import chardet
import PyPDF2
from docx import Document as DocxDocument
from werkzeug.utils import secure_filename
from typing import Tuple, Optional

logger = setup_logger(__name__)

def allowed_file(filename: str) -> bool:
    """Check if the file extension is allowed."""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS

def save_file(file, filename: str) -> Tuple[bool, Optional[str], Optional[str]]:
    """
    Save uploaded file to the upload directory.
    
    Returns:
        Tuple[bool, Optional[str], Optional[str]]: (success, file_path, error_message)
    """
    try:
        filename = secure_filename(filename)
        file_path = os.path.join(Config.UPLOAD_FOLDER, filename)
        file.save(file_path)
        return True, file_path, None
    except Exception as e:
        logger.error(f"Error saving file: {str(e)}")
        return False, None, str(e)

def detect_file_encoding(file_path: str) -> str:
    """Detect the encoding of a file."""
    try:
        with open(file_path, 'rb') as file:
            raw_data = file.read()
        return chardet.detect(raw_data)['encoding']
    except Exception as e:
        logger.error(f"Error detecting file encoding: {str(e)}")
        return 'utf-8'

def extract_text_from_file(file_path: str) -> str:
    """Extract text from various file formats."""
    try:
        if file_path.endswith('.pdf'):
            return extract_text_from_pdf(file_path)
        elif file_path.endswith('.docx'):
            return extract_text_from_docx(file_path)
        else:
            encoding = detect_file_encoding(file_path)
            with open(file_path, 'r', encoding=encoding) as f:
                return f.read()
    except Exception as e:
        logger.error(f"Error extracting text from {file_path}: {str(e)}")
        raise

def extract_text_from_pdf(file_path: str) -> str:
    """Extract text from PDF files."""
    try:
        text = ""
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page in pdf_reader.pages:
                text += page.extract_text()
        return text
    except Exception as e:
        logger.error(f"Error extracting text from PDF: {str(e)}")
        raise

def extract_text_from_docx(file_path: str) -> str:
    """Extract text from DOCX files."""
    try:
        doc = DocxDocument(file_path)
        return "\n".join([paragraph.text for paragraph in doc.paragraphs])
    except Exception as e:
        logger.error(f"Error extracting text from DOCX: {str(e)}")
        raise 