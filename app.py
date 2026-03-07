from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field,computed_field
from typing import List,Annotated,Literal
import pandas as pd
from schema.user_input import UserInput
from schema.prediction_response import PredictionResponse
from model.predict import model, scaler, MODEL_VERSION,predict_output


app=FastAPI()



# human readable endpoint
@app.get('/')
def read_root():
    return {"message": "Welcome to the Heart Disease Risk Prediction API. Use the /predict endpoint to get risk predictions."}  

# machine readable endpoint for health check
@app.get('/health')
def health_check():
    return {
        "status": "API is healthy and running.", 
        "model_version": MODEL_VERSION,"model_loaded": model is not None
        }

@app.post('/predict',response_model=PredictionResponse)
def predict_heart_disease_risk(data: UserInput):
    user_input={
        'age':data.age,
        'male':data.male,
        'cigsPerDay':data.cigsPerDay,
        'totChol':data.totChol,
        'sysBP':data.sysBP,
        'glucose':data.glucose
    }
    # prediction=model.predict(input_df)[0]

    # return JSONResponse(status_code=200,content={'heart_disease_risk': int(prediction)})

    
    try:
        prediction = predict_output(user_input)

        
        return JSONResponse(status_code=200, content={
            'response': prediction
            })
    except Exception as e:
        return JSONResponse(status_code=500, content={'error': str(e)})
    