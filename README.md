# Resume Analyzer 📝

## Overview

The **Resume Analyzer** is an intelligent web application designed to analyze uploaded resumes and provide suitable job title suggestions based on their content. By leveraging advanced natural language processing (NLP) techniques and embeddings, this tool helps job seekers better understand their qualifications and potential job opportunities.

Try out the live demo here:  
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ai-resumeanalyzer.streamlit.app/)

## Features

- **File Upload**: Supports multiple file formats including PDF, DOCX, and TXT for easy resume submission.
- **Job Title Suggestions**: Analyzes resume content to provide the top three job titles that match the candidate's qualifications.
- **User-Friendly Interface**: Built with Streamlit for a smooth and interactive user experience.
- **Integration with Hugging Face**: Utilizes state-of-the-art embedding models for accurate text analysis.
- **Groq Language Model**: Employs a powerful language model to enhance the analysis and suggestions.

## Technologies Used ⚙️

- **Python**: The primary programming language used for development.
- **Streamlit**: A framework for building the web application interface.
- **Hugging Face Transformers**: For embeddings and NLP tasks.
- **FAISS**: A library for efficient similarity search and clustering of dense vectors.
- **LlamaIndex**: A framework for handling vector stores and indexing.

## Installation ⏳

To run the Resume Analyzer locally, follow these steps:
**Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/resume-analyzer.git
   cd resume-analyzer
