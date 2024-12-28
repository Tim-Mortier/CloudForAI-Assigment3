import pickle
import numpy as np

def make_prediction(data: list[float]):
    # Load model (ensure path is correct)
    try:
        model = pickle.load(open("model.pkl", "rb"))
    except FileNotFoundError:
        raise FileNotFoundError("The model file 'model.pkl' was not found. Please ensure it is in the same directory.")
    
    # Prepare data and make prediction
    data = np.array(data).reshape(1, -1)
    prediction = model.predict(data)
    return prediction
