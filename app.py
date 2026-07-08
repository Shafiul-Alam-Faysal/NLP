import streamlit as st
from src.predict import predict_duplicate

st.title("Quora Duplicate Question Detector")

q1 = st.text_area("Question 1")
q2 = st.text_area("Question 2")

if st.button("Predict"):

    if not q1.strip() or not q2.strip():
        st.warning("Please enter both questions.")
    else:
        pred, prob = predict_duplicate(q1, q2)

        if pred == 1:
            st.success("Duplicate")
        else:
            st.error("Not Duplicate")

# import streamlit as st

# st.title("Hello World")

# st.success("Streamlit is working!")