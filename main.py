from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from prediction_model.predict import generate_predictions

app = FastAPI(
    title="Loan Prediction App using API - CI CD Jenkins",
    description="A Simple CI CD Demo",
    version='1.0'
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class LoanPrediction(BaseModel):
    Gender: str
    Married: str
    Dependents: str
    Education: str
    Self_Employed: str
    ApplicantIncome: float
    CoapplicantIncome: float
    LoanAmount: float
    Loan_Amount_Term: float
    Credit_History: float
    Property_Area: str

@app.get("/")
def index():
    return {"message": "Welcome to Loan Prediction App using API - CI CD Jenkins"}

@app.post("/prediction_api")
def predict(loan_details: LoanPrediction):
    data = loan_details.dict()
    prediction = generate_predictions([data])["prediction"][0]
    if prediction == "Y":
        pred = "Approved"
    else:
        pred = "Rejected"
    return {"status": pred}

@app.post("/prediction_ui")
def predict_gui(loan_details: LoanPrediction):
    data = loan_details.dict()
    prediction = generate_predictions([data])["prediction"][0]
    if prediction == "Y":
        pred = "Approved"
    else:
        pred = "Rejected"
    return {"status": pred}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)
