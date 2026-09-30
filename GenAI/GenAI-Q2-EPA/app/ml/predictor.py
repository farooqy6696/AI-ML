"""
ML Module — runtime predictor.
Loads the trained RandomForest model (training the default one on first
use if it doesn't exist yet) and exposes prediction + salary-outlier helpers.
"""
import os
import numpy as np
import joblib

from app.core.exceptions import MLModelException
from app.ml.train_model import MODEL_PATH, ENCODER_PATH, FEATURE_COLUMNS, train

TRAINING_RECOMMENDATIONS = {
    "Poor": [
        "Foundational skills bootcamp",
        "One-on-one mentorship program",
        "Attendance & time-management coaching",
    ],
    "Average": [
        "Intermediate technical certification",
        "Project management fundamentals",
        "Communication & collaboration workshop",
    ],
    "Good": [
        "Advanced specialization course in their domain",
        "Leadership & team-lead readiness program",
        "Cross-functional project rotation",
    ],
    "Excellent": [
        "Advanced leadership / management track",
        "Speaking or mentoring opportunities",
        "Stretch assignments on strategic initiatives",
    ],
}


class PerformancePredictor:
    def __init__(self):
        self._model = None
        self._encoder = None

    def _ensure_loaded(self):
        if self._model is not None and self._encoder is not None:
            return
        if not (os.path.exists(MODEL_PATH) and os.path.exists(ENCODER_PATH)):
            # Train a default model automatically on first run.
            train()
        try:
            self._model = joblib.load(MODEL_PATH)
            self._encoder = joblib.load(ENCODER_PATH)
        except Exception as exc:
            raise MLModelException(f"Failed to load ML model: {exc}")

    def predict(self, experience: float, attendance: float, projects_completed: int,
                num_skills: int = 5, num_certifications: int = 1):
        self._ensure_loaded()
        try:
            X = np.array([[experience, attendance, projects_completed, num_skills, num_certifications]])
            proba = self._model.predict_proba(X)[0]
            pred_idx = int(np.argmax(proba))
            category = self._encoder.inverse_transform([pred_idx])[0]
            confidence = float(proba[pred_idx])
            recommendations = TRAINING_RECOMMENDATIONS.get(category, [])
            return category, confidence, recommendations
        except Exception as exc:
            raise MLModelException(f"Prediction failed: {exc}")

    @staticmethod
    def detect_salary_outliers(employees: list, z_threshold: float = 2.0):
        """
        employees: list of dicts with keys 'employee_id', 'name', 'department', 'salary'.
        Flags salaries whose z-score (within their department) exceeds the threshold.
        """
        import pandas as pd

        if not employees:
            return []

        df = pd.DataFrame(employees)
        outliers = []
        for dept, group in df.groupby("department"):
            mean = group["salary"].mean()
            std = group["salary"].std(ddof=0) or 1e-9
            group = group.copy()
            group["z_score"] = (group["salary"] - mean) / std
            flagged = group[group["z_score"].abs() >= z_threshold]
            for _, row in flagged.iterrows():
                outliers.append(
                    {
                        "employee_id": int(row["employee_id"]),
                        "name": row["name"],
                        "department": dept,
                        "salary": float(row["salary"]),
                        "z_score": round(float(row["z_score"]), 2),
                    }
                )
        return outliers


performance_predictor = PerformancePredictor()
