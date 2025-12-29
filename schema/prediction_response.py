# Here, we'll be coding the respone model of the API.
from pydantic import BaseModel,Field
from typing import Annotated


class Prediction_response(BaseModel):
    predicted_category: Annotated[str,Field(...,description="The predicted category of the insurance premium",example="High")]
    confidence: Annotated[float,Field(...,description="The confidence level of the predicted label", example=0.48)]
    class_probabilities: Annotated[dict[str,float],Field(...,description="The probabilities of each class",example={"High":0.7,"Medium":0.48,"Low":0.67})]
