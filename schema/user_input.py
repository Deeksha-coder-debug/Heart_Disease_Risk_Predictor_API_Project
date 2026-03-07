from pydantic import BaseModel, Field,computed_field
from typing import List,Annotated,Literal
class UserInput(BaseModel):
    male: Annotated[Literal[0, 1], Field(...,description='Gender of the person i.e. 0 for female and 1 for male', example=1)]
    age: Annotated[int, Field(...,gt=0,lt=120,description='Age of the person', example=45)]
    education: Annotated[int, Field(...,description='Education level of the person i.e. 0 for high school, 1 for bachelor\'s degree, 2 for master\'s degree and 3 for doctorate', example=2)]
    currentSmoker: Annotated[Literal[0, 1], Field(...,description='Whether the person is a current smoker i.e. 0 for no and 1 for yes', example=0)]
    cigsPerDay: Annotated[int, Field(...,description='Number of cigarettes smoked per day', example=0)]
    BPMeds: Annotated[Literal[0, 1], Field(...,description='Whether the person is on blood pressure medication i.e. 0 for no and 1 for yes', example=0)]
    prevalentStroke: Annotated[Literal[0, 1], Field(...,description='Whether the person has had a stroke previously i.e. 0 for no and 1 for yes', example=0)]
    prevalentHyp: Annotated[Literal[0, 1], Field(...,description='Whether the person has hypertension i.e. 0 for no and 1 for yes', example=0)]
    diabetes: Annotated[Literal[0, 1], Field(...,description='Whether the person has diabetes i.e. 0 for no and 1 for yes', example=0)]
    totChol: Annotated[int, Field(...,description='Total cholesterol level of the person', example=200)]
    sysBP: Annotated[float, Field(...,description='Systolic blood pressure of the person', example=120.0)]
    diaBP: Annotated[float, Field(...,description='Diastolic blood pressure of the person', example=80.0)]
    BMI: Annotated[float, Field(...,description='Body mass index of the person', example=25.0)]
    heartRate: Annotated[int, Field(...,description='Heart rate of the person', example=70)]
    glucose: Annotated[int, Field(...,description='Glucose level of the person', example=100)]  