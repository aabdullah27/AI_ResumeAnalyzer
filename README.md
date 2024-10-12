# Resume Analyzer 📝

## Overview

The **Resume Analyzer** is an intelligent web application designed to analyze uploaded resumes and provide suitable job title suggestions based on their content. By leveraging advanced natural language processing (NLP) techniques and embeddings, this tool helps job seekers better understand their qualifications and potential job opportunities.

Try out the live demo here:  
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ai-resumeanalyzer.streamlit.app/)


## Features

- **File Upload**: Supports multiple file formats including PDF, DOCX, and TXT for easy resume submission.
- **Job Title Suggestions**: Analyzes resume content to provide the top three job titles that match the candidate's qualifications.
- **Experience Analysis**: Determines total years of experience and categorizes candidates as Junior, Mid-level, or Senior.
- **ATS Compatibility Score**: Provides a score out of 10 based on formatting, keyword usage, and structure.
- **Readability and Clarity Rating**: Rates the clarity of the resume on a scale of 1 to 10, with suggestions for improvement.
- **Top Projects/Accomplishments Extraction**: Identifies and highlights the top three projects or accomplishments listed in the resume.
- **User-Friendly Interface**: Built with Streamlit for a smooth and interactive user experience.
- **Integration with Hugging Face**: Utilizes state-of-the-art embedding models for accurate text analysis.
- **Groq Language Model**: Employs a powerful language model to enhance the analysis and suggestions.
- **Error Handling**: Provides user-friendly error messages for a seamless experience.


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
