# Heart Disease Risk Prediction API

A REST API built with **FastAPI** that predicts a user's heart disease risk level based on key health indicators, using a Logistic Regression model trained on the **Framingham Heart Study** dataset.Also includes streamlit frontend functionality where user can enter parameters and predict level of risk & percentage of risk.

---

## Features
- Predicts heart disease risk as **Low**, **Medium**, or **High**
- Returns confidence score and class probabilities
- Input validation via Pydantic
- Health check and versioning endpoints

---

## Tech Stack
- **Python**
- **FastAPI**
- **Scikit-learn** (Logistic Regression)
- **Pandas**
- **Pydantic**

---

## Project Structure
heart-disease-api/
├── app.py                  # FastAPI app and routes
├── model/
│   ├── predict.py          # Prediction logic
│   ├── logistic_regression_model.pkl
│   └── scaler.pkl
├── schema/
│   └── user_input.py       # Pydantic input schema
├── requirements.txt
└── README.md


---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Welcome message |
| GET | `/health` | API health check + model version |
| POST | `/predict` | Predict heart disease risk |

---

## Setup & Run

### 1. Clone the repo
git clone https://github.com/your-username/heart-disease-api.git
cd heart-disease-api

### 2. Install dependencies
pip install -r requirements.txt

### 3. Run the API
uvicorn app:app --reload

### 4. Open docs
Visit http://127.0.0.1:8000/docs for the interactive Swagger UI.

---

## Model Info
- **Algorithm:** Logistic Regression
- **Dataset:** Framingham Heart Study
- **Version:** 1.0.0
- **Scaled with:** StandardScaler

---

# 2nd Version details

# ❤️ Heart Disease Risk Prediction API with interactive Streamlit app functionality & Docker Containerization

A production-ready REST API built with **FastAPI** that predicts a user's heart disease
risk level based on key health indicators, using a Logistic Regression model trained on
the **Framingham Heart Study** dataset. Includes an interactive **Streamlit frontend** and full
**Docker containerization**.

---

## Features
- Predicts heart disease risk as **Low**, **Medium**, or **High**
- Returns confidence score and class probabilities
- Structured response via **Pydantic response models**
- Input validation via Pydantic
- Health check and model versioning endpoints
- Interactive **Streamlit UI** for non-technical users
- Fully **Dockerized** for easy deployment

---

## Tech Stack
- **Python**
- **FastAPI**
- **Streamlit**
- **Scikit-learn** (Logistic Regression)
- **Pandas**
- **Pydantic**
- **Docker**

---

## Project Structure
```
Serving ML Model FastAPI/
├── model/
│   ├── logistic_regression_model.pkl  # Trained ML model
│   ├── scaler.pkl                     # StandardScaler for preprocessing
│   └── predict.py                     # Prediction logic
├── schema/
│   ├── user_input.py                  # Pydantic input schema
│   └── prediction_response.py         # Pydantic response model
├── app.py                             # FastAPI app and routes
├── frontend.py                        # Streamlit UI
├── Dockerfile                         # Docker configuration
├── requirements.txt                   # Python dependencies
├── start.sh                           # Startup script
└── README.md
```

## Streamlit Frontend

The interactive UI allows non-technical users to:
- Enter personal and clinical health details across organized sections
- Submit inputs and receive a real-time risk prediction
- View risk level with color-coded indicators (🟢 Low / 🟡 Medium / 🔴 High)
- See confidence score displayed as a progress bar and metric

---

## Model Info
- **Algorithm:** Logistic Regression
- **Dataset:** Framingham Heart Study
- **Version:** 2.0.0
- **Preprocessing:** StandardScaler

---

## Author
Sai Deeksha Talabaktula — [github.com/Deeksha-coder-debug](https://github.com/Deeksha-coder-debug)

