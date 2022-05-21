import streamlit as st
import joblib
import pandas as pd

st.title("Prediction of bend deduction")
st.write("Enter the inputs")
# st.selectbox(
#     'Angle',
#     ('90', '100', '110','120', '130', '140', '150')
# )
angle = st.number_input("Angle",1.0,359.9)
thickness = st.number_input("Thickness",0.0,25.0)
vType = st.number_input("V Type",1.0,200.0)
pRadius = st.number_input("Punch",0.0,100.0)

model = joblib.load('model.pkl')
input = [[thickness, vType, pRadius, angle]]
bendDeduction = model.predict(input)
st.write("Bend Deduction :", bendDeduction[0])