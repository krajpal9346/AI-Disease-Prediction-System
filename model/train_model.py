import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv("../dataset/Training.csv")

# Split features and target
X = df.drop("prognosis", axis=1)
y = df["prognosis"]

# Encode labels
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# Train model
model = RandomForestClassifier(
    n_estimators=300,
    random_state=42
)
model.fit(X, y_encoded)

# Save files
joblib.dump(model, "disease_model.pkl")
joblib.dump(le, "label_encoder.pkl")
joblib.dump(list(X.columns), "features.pkl")

print("✅ Model training completed successfully")