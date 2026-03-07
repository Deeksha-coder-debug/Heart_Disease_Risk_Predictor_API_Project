import streamlit as st
import requests

API_URL = 'http://localhost:8000/predict'

st.title("Heart Disease Risk Prediction")

st.markdown('Enter your health details to predict your heart disease risk:')

# Collect user input
male = st.selectbox('Gender', options=[0, 1], format_func=lambda x: 'Female' if x == 0 else 'Male')
age = st.number_input('Age', min_value=1, max_value=120, value=45)
education = st.selectbox('Education Level', options=[0, 1, 2, 3], format_func=lambda x: ['High School', 'Bachelor\'s Degree', 'Master\'s Degree', 'Doctorate'][x])
currentSmoker = st.selectbox('Current Smoker', options=[0, 1], format_func=lambda x: 'No' if x == 0 else 'Yes')
cigsPerDay = st.number_input('Cigarettes Per Day', min_value=0, value=0)
BPMeds = st.selectbox('On Blood Pressure Medication', options=[0, 1 ], format_func=lambda x: 'No' if x == 0 else 'Yes')
prevalentStroke = st.selectbox('Previous Stroke', options=[0, 1], format_func=lambda x: 'No' if x == 0 else 'Yes')          
prevalentHyp = st.selectbox('Hypertension', options=[0, 1], format_func=lambda x: 'No' if x == 0 else 'Yes')
diabetes = st.selectbox('Diabetes', options=[0, 1], format_func=lambda x: 'No' if x == 0 else 'Yes')
totChol = st.number_input('Total Cholesterol', min_value=0, value=200)
sysBP = st.number_input('Systolic Blood Pressure', min_value=0.0, value=120.0)
diaBP = st.number_input('Diastolic Blood Pressure', min_value=0.0, value=80.0)
BMI = st.number_input('Body Mass Index', min_value=0.0, value=25.0)
heartRate = st.number_input('Heart Rate', min_value=0, value=70)    
glucose = st.number_input('Glucose Level', min_value=0, value=100)

if st.button('Predict Risk'):
    input_data={
        'male': male,
        'age': age,
        'education': education, 
        'currentSmoker': currentSmoker,
        'cigsPerDay': cigsPerDay,
        'BPMeds': BPMeds,
        'prevalentStroke': prevalentStroke,
        'prevalentHyp': prevalentHyp,
        'diabetes': diabetes,
        'totChol': totChol,
        'sysBP': sysBP,
        'diaBP': diaBP,
        'BMI': BMI,
        'heartRate': heartRate,
        'glucose': glucose
    }

try:
    response = requests.post(API_URL, json=input_data)
    if response.status_code == 200:
        result = response.json()
        st.success(f"Predicted Risk Level: **{result['risk_label']}** (Probability: **{result['probability']*100:.2f}**%)")
    else:
        st.error(f"Error: {response.status_code} - {response.text}")
except Exception as e:
    st.error(f"An error occurred: {e}")