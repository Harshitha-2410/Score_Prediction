from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
df=joblib.load("model/score_train_model.pkl")
class stu_data(BaseModel):
    study_time : float
    attendance : float
    gender_Male : int

app=FastAPI()
@app.get("/")
def root_data():
    return{"message":"Welcome"}
@app.post("/prd")
def score_pred(data:stu_data):
    inp=np.array([[data.study_time,data.attendance,data.gender_Male]])
    out=df.predict(inp)
    return {"Predicted score":int(out[0])}
