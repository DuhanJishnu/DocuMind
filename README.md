# DocuMind: Chat with Multiple PDFs using AI 🤖📚

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-00ADD8?style=for-the-badge&logo=LangChain&logoColor=white)
![Mistral](https://img.shields.io/badge/Mistral-041E27?style=for-the-badge)
![Groq](https://img.shields.io/badge/Groq-00ADD8?style=for-the-badge)

DocuMind is an intelligent chatbot powered by cutting-edge AI that lets you converse with multiple PDF documents simultaneously. Built with Mistral embeddings, Groq's lightning-fast LLM, and LangChain's RAG architecture.

**Live Demo**: [Coming Soon] | **Video Demo**: [Coming Soon]

## 🌟 Features

- **Multi-PDF Analysis**: Upload and chat with multiple PDFs simultaneously
- **RAG Architecture**: Advanced Retrieval Augmented Generation for context-aware responses
- **Mistral Embeddings**: State-of-the-art text embeddings for document understanding
- **Groq Accelerated AI**: Blazing-fast responses using Groq's LPU inference engine
- **Conversational Memory**: Remembers previous interactions in the chat session
- **Streamlit UI**: Clean and intuitive web interface

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- [Mistral API Key](https://console.mistral.ai/)
- [Groq API Key](https://console.groq.com/)
- Basic terminal knowledge

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/documind.git
cd documind
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Configuration

1. Create `.env` file in root directory:
```env
MISTRAL_API_KEY=your_mistral_api_key_here
GROQ_API_KEY=your_groq_api_key_here
```

2. **Never commit your .env file!**

### Running the App

```bash
streamlit run app.py
```

The app will automatically open in your default browser at `http://localhost:8501`

## 🧠 How It Works

1. **PDF Processing**  
   - Upload multiple PDFs through the sidebar
   - Text extraction using PyPDF2

2. **Text Chunking**  
   - Smart text splitting with overlap for context preservation

3. **Vector Storage**  
   - Mistral embeddings transform text into vectors
   - FAISS for efficient similarity search

4. **Conversational AI**  
   - Groq-powered Llama 3 8B Instant model
   - LangChain conversation chain with memory

5. **RAG Pipeline**  
   - Combines document retrieval with generative AI
   - Context-aware responses grounded in your documents

## 💻 Usage Guide

1. Open the sidebar (click ➡️ icon top-left)
2. Upload PDF files (multiple selection supported)
3. Click "PROCESS" to create knowledge base
4. Start chatting in the main interface!
5. Ask questions like:
   - "Summarize the key points from the reports"
   - "What did the financial document say about Q4 earnings?"
   - "Compare the technical specifications from both manuals"

## 🔧 Troubleshooting

**Common Issues:**
- API keys not found: Verify `.env` file exists with correct keys
- PDF parsing errors: Ensure documents are text-based (scanned PDFs not supported)
- Memory issues: Reduce number/size of PDFs if using limited hardware

## 📚 Technology Stack

| Component              | Technology Used          |
|------------------------|--------------------------|
| Language Model         | Groq/Llama-3.1-8b-instant|
| Text Embeddings        | Mistral-embed            |
| Vector Store           | FAISS                    |
| App Framework          | Streamlit                |
| Conversation Chain     | LangChain                |
| PDF Processing         | PyPDF2                   |


## 📜 License

MIT License - See [LICENSE](LICENSE) for details

---
