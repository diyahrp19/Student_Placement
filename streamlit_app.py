import streamlit as st
import pickle

# Load your model
model = pickle.load(open("model.pkl", "rb"))

st.title("Placement Predictor")

cgpa = st.slider("CGPA", 0.0, 10.0, 7.0)
aptitude = st.slider("Aptitude score", 0, 100, 70)
communication = st.slider("Communication", 1, 10, 5)
projects = st.slider("Projects", 0, 5, 2)

if st.button("Predict"):
    data = [[cgpa, aptitude, communication, projects]]
    prediction = model.predict(data)[0]  # assuming model returns 0 or 1

    if prediction == 1:
        st.success("You will be placed!")
    else:
        st.error("Not likely to be placed")