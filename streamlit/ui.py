import streamlit as st
import requests

st.title("Score Prediction")

stu = st.sidebar.slider("Study Time", 0, 10)
att = st.sidebar.slider("Attendance", 0, 100)
gen = st.sidebar.selectbox("Gender", ["Male", "Female"])
gender = 1 if gen == "Male" else 0

sub = st.sidebar.button("Predict")

if sub:
    st.write("Study Time:", stu)
    st.write("Attendance:", att)
    st.write("Gender:", gen)

    data = {
        "study_time": stu,
        "attendance": att,
        "gender_Male": gender
    }

    try:
        res = requests.post("https://score-prediction-2.onrender.com/prd", json=data)

        # Show raw response for debugging
        st.text(f"Response status code: {res.status_code}")
        st.text(f"Response content:\n{res.text}")

        if res.status_code == 200:
            try:
                result = res.json()
                st.success(f"Predicted score is: {result['Predicted score']}")
            except requests.exceptions.JSONDecodeError:
                st.error("❌ Response is not valid JSON. Check server response above.")
        else:
            st.error(f"❌ API returned error. Status code: {res.status_code}")

    except requests.exceptions.RequestException as e:
        st.error(f"❌ Could not connect to API: {e}")
