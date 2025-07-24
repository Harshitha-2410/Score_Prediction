import streamlit as st
import requests
st.title("Score Prediction")
stu=st.sidebar.slider("Study Time",0,10)
att=st.sidebar.slider("Attendance",0,100)
gen=st.sidebar.selectbox("Gender",["Male","Female"])
gender=1 if(gen=="Male") else 0
sub=st.sidebar.button("Predict")
if sub:
    st.write("Study Time:",stu)
    st.write("Attendance:",att)
    st.write("Gender:",gen)
    data={
    "study_time":stu,
    "attendance":att,
    "gender_Male":gender
    }
    res=requests.post("https://score-prediction-3.onrender.com/prd",json=data)
    result=res.json()
    st.write("Predicted score is:",result["Predicted score"])
