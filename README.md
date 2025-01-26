
---

# LangChain Projects with Streamlit

This repository contains multiple projects built using the **LangChain** framework and **Streamlit**. The projects demonstrate various applications of large language models (LLMs), including chatbots, conversational Q&A, and PDF text extraction, among others. Streamlit is used to build interactive and easy-to-use web interfaces for these applications.

---

## Projects

### 1. **Chatbots**
- A chatbot application built using LangChain and Streamlit, providing a simple interface for interacting with an AI-powered chatbot.
- Allows for dynamic conversation flows based on the user's input.

### 2. **Conversational Q&A Chatbot**
- A more advanced chatbot that supports context-aware question answering.
- The chatbot is able to respond based on provided information and can maintain the context of the conversation.

### 3. **PDF Extractor**
- A tool for extracting text from PDF files.
- Built using LangChain for processing and extracting relevant information, with an easy-to-use Streamlit interface for uploading and analyzing PDFs.

### 4. **Langserve**
- A project demonstrating the integration of LangChain models with a web server.
- Provides API-like functionality for interacting with large language models through a simple interface.

---

## Technologies Used

- **LangChain**: Framework for working with large language models (LLMs).
- **Streamlit**: Used for creating interactive UIs to showcase LangChain applications.
- **Python**: The primary programming language for building the backend and integrating with LangChain and Streamlit.
- **Other Libraries**: `pdfminer`, `openai`, `dotenv` (for environment variables), and more.

---

## Setup Instructions

### Prerequisites

- Python 3.x
- Streamlit
- LangChain
- Any required API keys (e.g., OpenAI)

### Steps to Set Up:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/langchain-streamlit.git
   cd langchain-streamlit
   ```

2. Set up a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the `.env` file in the root directory with your environment variables (like API keys, if needed):
   ```env
   OPENAI_API_KEY=your-openai-api-key-here
   ```

5. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

The application will be available at [http://localhost:8501](http://localhost:8501).

---

## License

MIT License

---
