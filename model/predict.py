import pickle 
import pandas as pd
#importing the model
with open('model/logistic_regression_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('model/scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

MODEL_VERSION = "1.0.0"

class_labels=["Low Risk","Medium Risk","High Risk"]
def predict_output(user_input:dict):
    input_df=pd.DataFrame([user_input])
    input_df = scaler.transform(input_df)

    probabilities = model.predict_proba(input_df)[0]
    
    output_prob = float(probabilities[1])  # probability of heart disease
    # output_prob=float(model.predict_proba(input_df)[0][1])  # probability of heart disease

    # class_probs=dict(zip(class_labels,map(lambda x: round(x,4),probabilities)))
    # Map probability to 3 risk levels
    if output_prob < 0.30:
        risk_label = "Low Risk"
    elif output_prob < 0.60:
        risk_label = "Medium Risk"
    else:
        risk_label = "High Risk"

    # return (risk_label, output_prob)

    return {
        'risk_label': risk_label,
        'confidence': round(output_prob,4),
        'class_probabilities': {
            'Low Risk': round(1 - output_prob, 4) if output_prob >= 0.30 else round(1 - output_prob, 4),
            'Medium Risk': round(output_prob, 4) if 0.30 <= output_prob < 0.60 else 0.0,
            'High Risk': round(output_prob, 4) if output_prob >= 0.60 else 0.0,
        }
    }
