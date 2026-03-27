import streamlit as st
import requests

st.title("Placement Predictor")

cgpa = st.slider("CGPA", 0.0, 10.0, 7.0, step=0.1)
aptitude = st.slider("Aptitude Score", 0, 100, 70, step=1)
communication = st.slider("Communication", 1, 10, 5, step=1)
projects = st.slider("Projects", 0, 5, 2, step=1)


if st.button("Predict"):
    url = "https://student-placement-2p4c.onrender.com/predict"  # Adjust if needed

    data = {
        "cgpa": cgpa,
        "aptitude": aptitude,
        "communication": communication,
        "projects": projects
    }

    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        result = response.json()

        if result.get('prediction') == 1:
            st.success("Student is likely to be Placed")
        else:
            st.error("Student is NOT likely to be Placed")
    except requests.exceptions.RequestException as e:
        st.error(f"Error contacting the server: {e}")
    except ValueError:
        st.error("Invalid response from server")