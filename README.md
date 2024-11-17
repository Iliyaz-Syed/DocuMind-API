
---

# **DocuMind API**

**DocuMind API** is a sophisticated Flask-based REST API crafted for intelligent document analysis leveraging LangChain and Large Language Models (LLMs). The system seamlessly processes various document formats (PDF, DOCX, TXT), generates embeddings using Ollama's LLM capabilities, and provides advanced text analysis features.

This API is built with a modular and maintainable architecture that prioritizes secure file handling, robust error management, and comprehensive logging. It exposes endpoints for document upload, analysis, listing, and deletion—making it ideal for applications requiring automated document understanding and analysis. By utilizing ChromaDB for vector storage and retrieval, the API ensures efficient semantic search and analysis capabilities.

---

## 🚀 **Features**

- **Document Processing**: Effortlessly upload and process PDF, DOCX, and TXT files.
- **Intelligent Analysis**: Summarize documents, extract key insights, and generate actionable recommendations.
- **Embeddings & Retrieval**: Generate and store embeddings for vector-based document retrieval and semantic search.
- **Secure & Robust**: Designed with error handling, logging, and file validation for optimal reliability.

---

## 🛠️ **Prerequisites**

Ensure you have the following installed before starting:

- **Python**: Version 3.8 or newer
- **Ollama**: For Large Language Model (LLM) support
- **Virtual Environment**: (Recommended) for dependency isolation

---

## 📥 **Installation**

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Iliyaz-Syed/DocuMind-API.git
   cd documentmind-api
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Ollama**:
   If Ollama is not installed, download it from the [official website](https://ollama.ai/) or install it using Homebrew (macOS):
   ```bash
   brew install ollama
   ```

5. **Pull the Llama Model**:
   After installing Ollama, pull the `llama3.2:latest` model:
   ```bash
   ollama pull llama3.2:latest
   ```

6. **Run the application**:
   ```bash
   flask run
   ```

---

## 🧑‍💻 **Usage**

1. **Upload a document**:  
   Send a POST request to `/upload` with your file.

2. **Analyze a document**:  
   Access analysis endpoints like `/analyze` for summarization, key point extraction, and more.

3. **List all documents**:  
   Use the `/list` endpoint to view uploaded files.

4. **Delete a document**:  
   Remove documents using the `/delete` endpoint.

---

## ⚙️ **Architecture**

The project is built using modern Python practices and a modular structure:
- **API Routes**: Defines endpoints and request handling logic.
- **Core Logic**: Encapsulates business functionality like text processing and embeddings.
- **Models**: Represents data structures for seamless handling.
- **Utilities**: Includes reusable helper functions for logging, validation, and more.

---

## 📚 **Technologies Used**

- **Flask**: Backend framework
- **LangChain**: Framework for LLM-based workflows
- **Ollama**: Embedding generation and LLM support
- **ChromaDB**: Vector database for semantic search

---

## 👩‍💻 **Contributing**

We welcome contributions! Follow these steps to contribute:
1. Fork the repository.
2. Create a new branch (`feature/your-feature`).
3. Commit your changes.
4. Push to your branch and create a pull request.

---

## 💬 **Contact**

For questions, suggestions, or feedback, feel free to reach out:
- **Email**: project.iliyaz@gmail.com
- **GitHub**: [Iliyaz Syed](https://github.com/Iliyaz-Syed)

---

### Built with ❤️ by [Iliyaz Syed](https://github.com/Iliyaz-Syed)