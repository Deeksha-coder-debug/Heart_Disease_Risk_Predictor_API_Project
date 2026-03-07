# Heart Disease Risk Prediction API

A REST API built with **FastAPI** that predicts a user's heart disease risk level based on key health indicators, using a Logistic Regression model trained on the **Framingham Heart Study** dataset.

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

## Input Features

| Field | Type | Description |
|---|---|---|
| `age` | int | Age of the patient |
| `male` | int | Sex (1 = Male, 0 = Female) |
| `cigsPerDay` | float | Cigarettes smoked per day |
| `totChol` | float | Total cholesterol level |
| `sysBP` | float | Systolic blood pressure |
| `glucose` | float | Blood glucose level |

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Welcome message |
| GET | `/health` | API health check + model version |
| POST | `/predict` | Predict heart disease risk |

---

## Sample Request

POST /predict
```json
{
  "age": 45,
  "male": 1,
  "cigsPerDay": 10,
  "totChol": 230,
  "sysBP": 140,
  "glucose": 85
}
```

## Sample Response
```json
{
  "risk_label": "Medium Risk",
  "confidence": 0.5821,
  "class_probabilities": {
    "Low Risk": 0.4179,
    "High Risk": 0.5821
  }
}
```

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

## Author
Your Name — [github.com/your-username](https://github.com/your-username)

