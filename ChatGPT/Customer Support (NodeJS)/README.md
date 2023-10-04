# **Answer Question System with GPT-3.5 Turbo and Flask**

## **Project Overview**

This project aims to create an "Answer Question System" utilizing the GPT-3.5 Turbo model by OpenAI. The system provides accurate and relevant answers to questions related to the content on the OpenAI website. The core of the system is built on a Flask application, exposing a REST API endpoint (`/ask`) that processes user questions using GPT-3.5 Turbo and generates appropriate responses.

## **Features**

- Utilizes OpenAI's **GPT-3.5 Turbo model** to generate responses for user questions.
- Provides an easy-to-use **REST API** for integrating with external applications.
- Enhances user interaction by enabling seamless integration with **Node.js applications**.

## **Components**

- **Flask Application**: The core application built using Flask to process and respond to user questions using GPT-3.5 Turbo.
- **GPT-3.5 Turbo Model**: The OpenAI GPT-3.5 Turbo model powers the question-answering capabilities of the system.
- **Node.js Integration**: Enables integration with Node.js applications, enhancing the system's user interaction capabilities.

## **Getting Started**

### **Prerequisites**

- OpenAI **GPT-3.5 Turbo API key**.
- **Python 3.x and pip** for running the Flask application.
- **Node.js and npm** for integrating with Node.js applications.

### **Setup**

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your-username/answer-question-system.git
    ```

2. Navigate to the project directory:

    ```bash
    cd answer-question-system
    ```

3. Install Python dependencies for the Flask application:

    ```bash
    pip install -r requirements.txt
    ```

4. Install Node.js dependencies for the Node.js integration:

    ```bash
    cd nodejs-integration
    npm install
    ```

### **Usage**

1. Run the Flask application:

    ```bash
    python app.py
    ```

2. Access the REST API endpoint at [http://localhost:5000/ask](http://localhost:5000/ask).

3. Integrate the API with your Node.js application using the provided integration in the `nodejs-integration` directory.

4. Send POST requests to the `/ask` endpoint with questions to receive responses.

## **API Documentation**

### **Endpoint**

**POST /ask**

### **Request Body**

```json
{
  "question": "What is GPT-3.5 Turbo?",
  "context": "Additional context or information related to the question."
}
