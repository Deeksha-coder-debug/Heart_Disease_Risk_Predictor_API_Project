# import streamlit as st
# import requests

# API_URL = 'http://127.0.0.1:8000/predict'

# st.title("Heart Disease Risk Prediction")

# st.markdown('Enter your health details to predict your heart disease risk:')

# # Collect user input
# male = st.selectbox('Gender', options=[0, 1], format_func=lambda x: 'Female' if x == 0 else 'Male')
# age = st.number_input('Age', min_value=1, max_value=120, value=45)
# education = st.selectbox('Education Level', options=[0, 1, 2, 3], format_func=lambda x: ['High School', 'Bachelor\'s Degree', 'Master\'s Degree', 'Doctorate'][x])
# currentSmoker = st.selectbox('Current Smoker', options=[0, 1], format_func=lambda x: 'No' if x == 0 else 'Yes')
# cigsPerDay = st.number_input('Cigarettes Per Day', min_value=0, value=0)
# BPMeds = st.selectbox('On Blood Pressure Medication', options=[0, 1 ], format_func=lambda x: 'No' if x == 0 else 'Yes')
# prevalentStroke = st.selectbox('Previous Stroke', options=[0, 1], format_func=lambda x: 'No' if x == 0 else 'Yes')          
# prevalentHyp = st.selectbox('Hypertension', options=[0, 1], format_func=lambda x: 'No' if x == 0 else 'Yes')
# diabetes = st.selectbox('Diabetes', options=[0, 1], format_func=lambda x: 'No' if x == 0 else 'Yes')
# totChol = st.number_input('Total Cholesterol', min_value=0, value=200)
# sysBP = st.number_input('Systolic Blood Pressure', min_value=0.0, value=120.0)
# diaBP = st.number_input('Diastolic Blood Pressure', min_value=0.0, value=80.0)
# BMI = st.number_input('Body Mass Index', min_value=0.0, value=25.0)
# heartRate = st.number_input('Heart Rate', min_value=0, value=70)    
# glucose = st.number_input('Glucose Level', min_value=0, value=100)

# if st.button('Predict Risk'):
#     input_data={
#         'male': male,
#         'age': age,
#         'education': education, 
#         'currentSmoker': currentSmoker,
#         'cigsPerDay': cigsPerDay,
#         'BPMeds': BPMeds,
#         'prevalentStroke': prevalentStroke,
#         'prevalentHyp': prevalentHyp,
#         'diabetes': diabetes,
#         'totChol': totChol,
#         'sysBP': sysBP,
#         'diaBP': diaBP,
#         'BMI': BMI,
#         'heartRate': heartRate,
#         'glucose': glucose
#     }

# try:
#     response = requests.post(API_URL, json=input_data)
#     if response.status_code == 200:
#         result = response.json()['response']
#         st.success(f"Predicted Risk Level: **{result['risk_label']}** (Probability: **{result['confidence']*100:.2f}**%)")
#     else:
#         st.error(f"Error: {response.status_code} - {response.text}")
# except Exception as e:
#     st.error(f"An error occurred: {e}")

import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict"

# Page configuration
st.set_page_config(
    page_title="Heart Disease Risk Predictor",
    page_icon="❤️",
    layout="wide"
)

# Title
st.title("❤️ Heart Disease Risk Prediction")
st.markdown("AI-powered cardiovascular risk assessment")

# Sidebar
st.sidebar.header("About")
st.sidebar.info(
"""
This tool predicts the **risk of heart disease** based on
clinical indicators.

⚕️ Model: Logistic Regression  
🧠 Version: 1.0  
"""
)

st.sidebar.header("Instructions")
st.sidebar.write(
"""
1. Enter your health information  
2. Click **Predict Risk**  
3. View your risk assessment
"""
)

# -------------------------------
# PERSONAL INFORMATION
# -------------------------------

st.subheader("👤 Personal Information")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=18, max_value=120, value=45)
    male = st.selectbox("Gender", [0,1], format_func=lambda x: "Female" if x==0 else "Male")
    education = st.selectbox(
        "Education Level",
        [0,1,2,3],
        format_func=lambda x: ["High School","Bachelor's","Master's","Doctorate"][x]
    )

with col2:
    heartRate = st.number_input("Heart Rate", value=70)
    glucose = st.number_input("Glucose Level", value=100)
    BMI = st.number_input("Body Mass Index", value=25.0)

# -------------------------------
# LIFESTYLE FACTORS
# -------------------------------

st.subheader("🚬 Lifestyle Factors")

col3, col4 = st.columns(2)

with col3:
    currentSmoker = st.selectbox("Current Smoker", [0,1], format_func=lambda x: "No" if x==0 else "Yes")
    cigsPerDay = st.number_input("Cigarettes Per Day", value=0)

with col4:
    diabetes = st.selectbox("Diabetes", [0,1], format_func=lambda x: "No" if x==0 else "Yes")
    BPMeds = st.selectbox("Blood Pressure Medication", [0,1], format_func=lambda x: "No" if x==0 else "Yes")

# -------------------------------
# MEDICAL METRICS
# -------------------------------

st.subheader("🩺 Medical Metrics")

col5, col6 = st.columns(2)

with col5:
    totChol = st.number_input("Total Cholesterol", value=200)
    sysBP = st.number_input("Systolic Blood Pressure", value=120.0)

with col6:
    diaBP = st.number_input("Diastolic Blood Pressure", value=80.0)
    prevalentHyp = st.selectbox("Hypertension", [0,1], format_func=lambda x: "No" if x==0 else "Yes")

# --------------------------------
# PREDICT BUTTON
# --------------------------------

if st.button("🔍 Predict Risk", use_container_width=True):

    input_data = {
        "male": male,
        "age": age,
        "education": education,
        "currentSmoker": currentSmoker,
        "cigsPerDay": cigsPerDay,
        "BPMeds": BPMeds,
        "prevalentStroke": 0,
        "prevalentHyp": prevalentHyp,
        "diabetes": diabetes,
        "totChol": totChol,
        "sysBP": sysBP,
        "diaBP": diaBP,
        "BMI": BMI,
        "heartRate": heartRate,
        "glucose": glucose
    }

    try:
        response = requests.post(API_URL, json=input_data)

        if response.status_code == 200:

            result = response.json()['response']

            risk = result["risk_label"]
            prob = result["confidence"]

            st.divider()
            st.subheader("📊 Risk Assessment Result")

            # Progress bar
            st.progress(prob)

            # Display result
            if risk == "Low Risk":
                st.success(f"🟢 **Low Risk** ({prob*100:.2f}%)")

            elif risk == "Medium Risk":
                st.warning(f"🟡 **Medium Risk** ({prob*100:.2f}%)")

            else:
                st.error(f"🔴 **High Risk** ({prob*100:.2f}%)")

            # Metrics display
            col7, col8 = st.columns(2)

            with col7:
                st.metric("Predicted Risk Level", risk)

            with col8:
                st.metric("Probability", f"{prob*100:.2f}%")

        else:
            st.error(f"API Error: {response.status_code}")

    except Exception as e:
        st.error(f"Connection error: {e}")


    st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #0f172a;
        color: white;
        text-align: center;
        padding: 10px;
        font-size: 16px;
        font-family: Arial;
    }
    </style>

    <div class="footer">
        With ❤️ Sai Deeksha Talabaktula | ML & Deep Learning Enthusiast
    </div>
    """,
    unsafe_allow_html=True
)