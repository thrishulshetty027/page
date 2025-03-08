import streamlit as st
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
    if firstname and lastname and agree and uploaded_file and workfields and course and gender :
        st.success(f"Thankyou, Mr/Ms. {firstname} {lastname}! your form has been submitted.")
        import time
        progress_bar = st.progress(0.0) 
        status_text = st.empty()
        for percent_complete in range(101):
            time.sleep(0.05)  
            progress_bar.progress(percent_complete /100.0)  
            status_text.text(f"Progress: {percent_complete}%")
            
        st.success("Task completed,successfullly!")

else:
    st.error("Please fill in all details and agree to the terms & conditions before submitting.")


