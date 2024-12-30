# CloudForAI-Assigment3
## Overview

This project is a machine learning prediction API built using FastAPI. The API allows users to make predictions using a pre-trained logistic regression model, which is trained on the heart disease dataset (`heart.csv`). It also supports easy deployment using Docker for production-grade setups.

## Setup and Installation
### Prerequisites

- Python 3.10+
- Docker (optional, for containerized deployment)

### Steps to Run Locally

1. Clone the repository:

    ```
    git clone https://github.com/Tim-Mortier/CloudForAI-Assigment3.git
    cd CloudForAI-Assigment3
    ```

2. Install dependencies:

    ```
    pip install -r requirements.txt
    ```

3. Train the model and generate model.pkl:

    ```
    python model.py
    ```

4. Start the API server:

    ```
    uvicorn app.main:app --reload
    ```

5. Open your browser and visit http://127.0.0.1:8000/docs to explore the API using Swagger UI.

## API Endpoints

1. GET `/`

    Returns a welcome message and guidance for using the /predict endpoint.

    Response:

    ```
    {
        "message": "Welcome to the prediction API! Use the /predict endpoint to make predictions."
    }
    ```

2. POST `/predict`

    Accepts a JSON object with input data for prediction.

    Request Body:

    ```
    {
        "data": [63, 1, 3, 145, 233, 1, 0, 150, 0, 2.3, 0, 0, 1]
    }   
    ```

    Response:

    ```
    {
        "prediction": [1]
    }
    ```

3. GET `/favicon.ico`
    
    Serves the favicon for the application.

## Testing the API

You can test the API using `curl` or tools like Postman.

### Example Curl Command:

```
curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d "{\"data\": [63, 1, 3, 145, 233, 1, 0, 150, 0, 2.3, 0, 0, 1]}"
```

## Docker Support

Building and Running the Docker Image

1. Build the Docker image:

    ```
    docker build -t fastapi-predictor .
    ```

2. Run the Docker container:

    ```
    docker run -p 8000:8000 fastapi-predictor
    ```

3. Access the API at `http://127.0.0.1:8000`.

This README provides all the necessary details to get started with the FastAPI Prediction API. Let me know if you need additional sections or enhancements!