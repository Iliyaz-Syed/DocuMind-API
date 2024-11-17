from flask import Request
from typing import Tuple, Optional
from app.utils.file_handlers import allowed_file

def validate_upload_request(request: Request) -> Tuple[bool, Optional[str]]:
    """
    Validate file upload request.
    
    Returns:
        Tuple[bool, Optional[str]]: (is_valid, error_message)
    """
    if 'file' not in request.files:
        return False, "No file part"
    
    file = request.files['file']
    if file.filename == '':
        return False, "No selected file"
        
    if not allowed_file(file.filename):
        return False, "File type not allowed"
    
    return True, None 