import pandas as pd
import joblib

model = joblib.load("disease_model.pkl")
le = joblib.load("label_encoder.pkl")

df_test = pd.read_csv("../dataset/Testing.csv")

X_test = df_test.drop("prognosis", axis=1)
y_test = le.transform(df_test["prognosis"])

accuracy = model.score(X_test, y_test)
print("Model Accuracy:", round(accuracy * 100, 2), "%")