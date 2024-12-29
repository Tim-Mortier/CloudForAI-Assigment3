import pickle
import pandas as pd
from sklearn.linear_model import LogisticRegression

def train_model():
    """
    Train a Logistic Regression model using the heart.csv dataset
    and save it as a pickle file.
    """
    df = pd.read_csv("heart.csv")
    X = df.drop("output", axis=1)
    y = df["output"]

    model = LogisticRegression()
    model.fit(X, y)

    with open("model.pkl", "wb") as model_file:
        pickle.dump(model, model_file)

if __name__ == "__main__":
    train_model()
