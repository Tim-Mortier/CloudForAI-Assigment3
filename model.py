import pickle
from sklearn.linear_model import LogisticRegression
import pandas as pd

df = pd.read_csv("heart.csv")
X = df.drop("output", axis=1)
y = df["output"]

model = LogisticRegression()
model.fit(X, y)

pickle.dump(model, open("model.pkl", "wb"))

