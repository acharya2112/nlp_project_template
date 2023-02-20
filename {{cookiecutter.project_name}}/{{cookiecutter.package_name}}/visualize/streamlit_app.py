import streamlit as st


mode = st.selectbox("Select Mode", ("Train", "Predict"))

uploaded_file = st.file_uploader("Choose a file", type=["pdf", "xlsx", "docx"])

if uploaded_file is not None:
    # Do something
    ...

if st.button("Button1"):
    # Do something
    ...

if st.button("Button2"):
    # Do something
    ...
