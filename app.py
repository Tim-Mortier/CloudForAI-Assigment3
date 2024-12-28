from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from predictor import make_prediction
import uvicorn

app = FastAPI()

# Request schema for prediction
class PredictionInput(BaseModel):
    data: list[float]

@app.get("/")
def read_root():
    return {"message": "Welcome to the prediction API! Use the /predict endpoint to make predictions."}

@app.get("/favicon.ico")
def get_favicon():
    return FileResponse("static/favicon.ico")

@app.post("/predict")
def predict(input_data: PredictionInput):
    prediction = make_prediction(input_data.data)
    return {"prediction": prediction.tolist()}  # Convert numpy array to list for JSON serialization

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
