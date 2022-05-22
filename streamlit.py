import streamlit as st
import joblib
import pandas as pd

st.title("Prediction of bend deduction")

st.write("##### The Bend Deduction is the difference between the sum of the flange lengths (from edge to the apex) and the initial flat length. In other words, the material you will have to remove from the total length of the flanges in order to arrive at the proper length in the flat pattern")

st.sidebar.write("### Enter the inputs")
angle = st.sidebar.number_input("Angle (in degrees)",1.0,359.9)
thickness = st.sidebar.number_input("Thickness (in mm)",0.0,25.0)
vType = st.sidebar.number_input("V Type (in mm)",1.0,200.0)
pRadius = st.sidebar.number_input("Punch (in mm)",0.0,100.0)

submit = st.sidebar.button('Calculate')

if submit:
    model = joblib.load('model.pkl')
    input = [[thickness, vType, pRadius, angle]]
    bendDeduction = model.predict(input)
    st.write(" ## Bend Deduction : {:0.2f}".format(bendDeduction[0]))
else:
    st.write(" ## Bend Deduction :") 