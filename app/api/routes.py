from flask import Blueprint, request, jsonify
from app.core.document_processor import DocumentProcessor
from app.core.document_analyzer import DocumentAnalyzer
from app.api.validators import validate_upload_request
from app.utils.file_handlers import save_file
from app.config.settings import Config
from app.utils.logger import setup_logger
import os
import shutil

logger = setup_logger(__name__)
api = Blueprint('api', __name__)

@api.route('/upload', methods=['POST'])
def upload_file():
    try:
        # Validate request
        is_valid, error_message = validate_upload_request(request)
        if not is_valid:
            return jsonify({"error": error_message}), 400

        file = request.files['file']
        
        # Save file
        success, file_path, error = save_file(file, file.filename)
        if not success:
            return jsonify({"error": error}), 500
            
        # Process document
        embed_folder = os.path.join(Config.EMBED_FOLDER, os.path.splitext(file.filename)[0])
        os.makedirs(embed_folder, exist_ok=True)
        
        processor = DocumentProcessor(embed_folder)
        success, error = processor.process_document(file_path)
        
        if not success:
            return jsonify({"error": error}), 500
            
        return jsonify({"message": "File uploaded and processed successfully"}), 200

    except Exception as e:
        logger.error(f"Error in upload_file: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

@api.route('/analyze/<filename>', methods=['POST'])
def analyze_document(filename):
    try:
        query = request.json.get('query', '''
            Provide a comprehensive analysis of the document including:
            1. Document summary
            2. Key points and findings
            3. Recommendations or action items
            ''')

        embed_folder = os.path.join(Config.EMBED_FOLDER, os.path.splitext(filename)[0])
        
        if not os.path.exists(embed_folder):
            return jsonify({"error": "Document embeddings not found"}), 404

        analyzer = DocumentAnalyzer(embed_folder)
        success, result, error = analyzer.analyze(query)
        
        if not success:
            return jsonify({"error": error}), 500
            
        return jsonify(result), 200

    except Exception as e:
        logger.error(f"Error in analyze_document: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

# Add other routes (list_documents, delete_document) similarly... 