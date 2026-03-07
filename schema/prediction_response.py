from pydantic import BaseModel, Field,computed_field
from typing import List,Annotated,Literal

class PredictionResponse(BaseModel):
    risk_label: str = Field(..., description='Risk label indicating the likelihood of heart disease (e.g., "Low Risk","Medium Risk", "High Risk")')
    confidence: float = Field(..., description="Model's confidence in the prediction, represented as a probability between 0 and 1)")
    class_probabilities: dict = Field(..., description="A dictionary containing the probabilities for each risk class (e.g., {'Low Risk': 0.7, 'Medium Risk': 0.2, 'High Risk': 0.1})")