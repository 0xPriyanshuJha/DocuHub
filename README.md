# DocuBot

## Overview

The **DocuBot** is a web app that enables users to upload PDF files, extract text from them, store the text in a vector database, and interact with the content using an Ollama language model. The application is containerized using Docker to ensure consistent deployment and environment setup.

## Features

- Upload and process PDF files.
- Extract and chunk text from PDFs.
- Store and index text using Chroma vector database.
- Query the content of the PDF using an Ollama language model.
- Deployable in a Docker container.

## Prerequisites

- Python 3.11 or higher
- Docker (for containerization)

## Setup Instructions

### 1. **Clone the Repository**

Clone this repository to your local machine:

```bash
git clone https://github.com/0xpriyanshujha/Docuhub.git
cd Docuhub
```
### 2. Create and Activate a Virtual Environment
Create a virtual environment to manage dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies
Install the required Python packages:
```bash
pip install -r requirements.txt
```

### 4. Docker Setup
If you want to run the application in a Docker container:
Build the Docker Image
```bash
docker build -t Docuhub .
Run the Docker Container
```

```bash
docker run -p 8501:8501 Docuhub
The application will be available at http://localhost:8501.
```

### Usage Instructions
* Upload a PDF File
* Open the application in your web browser.
* Use the file uploader widget to upload a PDF file.
* Query the PDF
* After uploading, type your query in the text input field.
* Click the submit button to get answers based on the content of the PDF.
* Interaction with PDF Content
* The application extracts text from the PDF, indexes it in Chroma, and uses the Ollama model to answer queries about the content.
  
##
<img width="1466" alt="Screenshot 2024-09-13 at 7 48 34 PM" src="https://github.com/user-attachments/assets/b7b534ca-3840-4d69-8296-46d4df386ab2">

##

<img width="905" alt="Screenshot 2024-09-13 at 7 48 44 PM" src="https://github.com/user-attachments/assets/4084b1bd-2d86-4e85-a370-8fdf3ed6a32c">
