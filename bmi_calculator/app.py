import streamlit as st 
import pandas as pd 
import time as t

st.title("BMI CALCULATOR")

feet = st.slider("Select your height in Feet", 4, 8, 4)
inches = st.slider("Select your height in Inches", 0, 11, 11) 
weight = st.slider("Select your weight in Kilograms", 0, 200, 70)

height_in_feet = feet + inches / 12

height_in_meters = height_in_feet * 0.3048

if st.button("Calculate BMI"):
    with st.spinner("Calculating your BMI..."):
        t.sleep(3)
    bmi = weight/(height_in_meters **2)
    st.success(f"Your BMI is: {bmi:.3f} ") 
    # st.subtitle("BMI Category":)
    if bmi > 18.5 :
        st.success("You are Underweight") 
    elif bmi < 18.5 and bmi > 24.9:
        st.success("You are Normal weight")
    elif bmi < 24.9 and bmi > 29.9:
        st.success("You are Overweight")
    else:
        st.success("You are Obese")
