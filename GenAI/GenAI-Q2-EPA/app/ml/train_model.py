"""
ML Module — offline training script.

Trains a RandomForest classifier that predicts an employee's performance
category (Poor / Average / Good / Excellent) from features:
experience, attendance, projects_completed, num_skills, num_certifications.

Run manually (or via a scheduled job) whenever you want to refresh the model:
    python -m app.ml.train_model

If no historical CSV is supplied, a small synthetic dataset is generated so
the API has a working model out of the box; replace with real employee data
for production use.
"""
import os
import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

MODEL_DIR = os.path.join(os.path.dirname(__file__), "artifacts")
MODEL_PATH = os.path.join(MODEL_DIR, "performance_model.joblib")
ENCODER_PATH = os.path.join(MODEL_DIR, "label_encoder.joblib")

FEATURE_COLUMNS = ["experience", "attendance", "projects_completed", "num_skills", "num_certifications"]


def _categorize(score: float) -> str:
    if score < 40:
        return "Poor"
    if score < 65:
        return "Average"
    if score < 85:
        return "Good"
    return "Excellent"


def generate_synthetic_dataset(n: int = 800, seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    experience = rng.uniform(0, 20, n)
    attendance = rng.uniform(50, 100, n)
    projects = rng.integers(0, 30, n)
    num_skills = rng.integers(1, 15, n)
    num_certs = rng.integers(0, 8, n)

    score = (
        0.35 * (experience / 20 * 100)
        + 0.30 * attendance
        + 0.20 * (projects / 30 * 100)
        + 0.10 * (num_skills / 15 * 100)
        + 0.05 * (num_certs / 8 * 100)
    ) + rng.normal(0, 5, n)
    score = np.clip(score, 0, 100)

    df = pd.DataFrame(
        {
            "experience": experience,
            "attendance": attendance,
            "projects_completed": projects,
            "num_skills": num_skills,
            "num_certifications": num_certs,
            "performance_score": score,
        }
    )
    df["performance_category"] = df["performance_score"].apply(_categorize)
    return df


def train(csv_path: str = None):
    os.makedirs(MODEL_DIR, exist_ok=True)

    if csv_path and os.path.exists(csv_path):
        df = pd.read_csv(csv_path)
    else:
        df = generate_synthetic_dataset()

    X = df[FEATURE_COLUMNS]
    y = df["performance_category"]

    encoder = LabelEncoder()
    y_encoded = encoder.fit_transform(y)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y_encoded, test_size=0.2, random_state=42, stratify=y_encoded
    )

    clf = RandomForestClassifier(n_estimators=200, max_depth=8, random_state=42)
    clf.fit(X_train, y_train)

    accuracy = clf.score(X_test, y_test)
    print(f"Model trained. Test accuracy: {accuracy:.3f}")

    joblib.dump(clf, MODEL_PATH)
    joblib.dump(encoder, ENCODER_PATH)
    print(f"Saved model -> {MODEL_PATH}")
    print(f"Saved label encoder -> {ENCODER_PATH}")


if __name__ == "__main__":
    train()
