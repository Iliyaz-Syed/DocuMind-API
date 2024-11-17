import os
import requests
from PyPDF2 import PdfReader
from docx import Document as docxDoc
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma 
from langchain.schema import Document

def extract_text(file_path):
    extension = os.path.splitext(file_path)[1].lower()
    if extension == '.pdf':
        return "\n".join(page.extract_text() for page in PdfReader(file_path).pages if page.extract_text())
    elif extension == '.docx':
        return "\n".join(para.text for para in docxDoc(file_path).paragraphs)
    elif extension == '.txt':
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    else:
        raise ValueError("Unsupported file format")

def chunk_text(text, chunk_size=1000, chunk_overlap=200):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return text_splitter.split_text(text)

def get_nomic_embedding(text):
    headers = {"Content-Type": "application/json"}
    try:
        response = requests.post(
            "http://192.165.134.27:23384/api/embed",
            json={"model": "nomic-embed-text:latest", "input": text},
            headers=headers
        )
        # print(response.json())
        response.raise_for_status()
        return response.json()['embeddings'][0]
    except requests.RequestException as req_err:
        print(f"Error fetching embedding: {req_err}")
        return None

class OllamaEmbeddings:
    def embed_documents(self, texts):
        return [get_nomic_embedding(text) for text in texts if get_nomic_embedding(text) is not None]

    def embed_query(self, text):
        return get_nomic_embedding(text)

def process_file(file_path, embed_folder):
    text = extract_text(file_path)
    if text:
        chunks = chunk_text(text)
        
        embedding_function = OllamaEmbeddings()
        
        vector_store = Chroma(persist_directory=embed_folder, embedding_function=embedding_function)
        
        documents = [Document(page_content=chunk, metadata={"id": f"chunk_{i}"}) for i, chunk in enumerate(chunks)]
        vector_store.add_documents(documents)
        return "OK"
    else:
        print("No text extracted from the file.")
        return "NOT OK"



if __name__ == "__main__":
    file_path = "/Users/iliyas/Documents/CodeLabs/crewai/autogen/md.pdf".strip()
    if os.path.exists(file_path):
        process_file(file_path)
    else:
        print(f"File not found: {file_path}")