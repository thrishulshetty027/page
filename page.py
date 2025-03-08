import streamlit as st
import pandas as pd
import os
import time
from pathlib import Path

secure_folder = "secure_data"
Path(secure_folder).mkdir(parents=True, exist_ok=True)

firstname=st.text_input("First name:")
st.write(f"{firstname}")
lastname=st.text_input("Last name:")
st.write(f"{lastname}")

age=st.slider("Select age",min_value=15,max_value=50)
st.write(f" Entered age : {age}")

gender=st.radio("Select Gender :",["Male","Female","Others"])
st.write(f"selected : {gender}")

course=st.radio("Select your Profession :",["Un.grad","Post.grad","Ph.D","Working"])
st.write(f"Profession : {course}")

workfields=st.selectbox("select your prefered work field",["data analyst","research","marketing","managment"])
st.write(f"Workfield : {workfields}")


uploaded_file=st.file_uploader("upload Resume in pdf file format",type=["pdf","jpg","txt"])
if uploaded_file is not None:
    st.success(f"file Uploaded sucessfully!")
    st.write("file name:",uploaded_file.name)

agree=st.checkbox("I agree to the terms&condition")
if agree:
    st.write("thankyou for agreeing")
else:
    st.error("agreed to the terms and condition by clicking the Box")

with st.form(key='my_form'):
    st.write("all the entered details are valid")
    submit=st.form_submit_button("Submit")

if submit:
    missing_fields =[]

    if not firstname:
        missing_fields.append("Enter First name")
    if not lastname:
        missing_fields.append("Enter Last name")
    if not uploaded_file:
        missing_fields.append("upload Resume")
    if not agree:
        missing_fields.append("Agree to Terms & Conditions")
        
    if missing_fields:
        st.warning(f"Form not filled completely")
    else:
        st.success(f"Thank you, Mr/Ms. {firstname} {lastname}! Your form has been submitted.")


    data={
        "First Name": firstname,
        "Last Name": lastname,
        "Age": age,
        "Gender": gender,
        "Profession": course,
        "Work Field": workfields,
        "Resume": uploaded_file.name if uploaded_file else "No file uploaded"
    }
    file_path = os.path.join(secure_folder, "user_data.csv")
    try:
        existing_data = pd.read_csv(file_path)
        updated_data = pd.concat([existing_data, pd.DataFrame([data])], ignore_index=True)
    except FileNotFoundError:
        updated_data = pd.DataFrame([data])
        updated_data.to_csv(file_path, index=False)
        
    progress_bar = st.progress(0)
    status_text = st.empty()

    if missing_fields:
        for percent_complete in range(81):
            time.sleep(0.02)
            progress_bar.progress(percent_complete)
            status_text.text(f"Progress: {percent_complete}%")

        st.warning(f" Please fill in the following fields before submitting: {', '.join(missing_fields)}")
    else:
        for percent_complete in range(101):
            time.sleep(0.02)
            progress_bar.progress(percent_complete)
            status_text.text(f"Progress: {percent_complete}%")
        st.success("data saved successfully")  
             
if st.button("Show Saved Data"):
    try:
        df = pd.read_csv("user_data.csv")
        st.write("### Saved Data")
        st.dataframe(df)  
    except FileNotFoundError:
        st.error("No data found. The CSV file doesn't exist yet.")

