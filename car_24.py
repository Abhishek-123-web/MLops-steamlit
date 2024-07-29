import streamlit as st
import pandas as pd
import pickle


st.title("Car Price Prediction App")

col1, col2 = st.columns(2)

with col1:
    fuel_type = st.radio("Fuel Type", ["Petrol", "Diesel", "CNG"])

with col2:
    transmission_type = st.selectbox("Transmission Type", ["Manual", "Automatic"])  

col3, col4 = st.columns(2)

with col3:
    Engine_power = st.slider("Engine Power", 500, 5000, step = 100)

with col4:
    seats = st.selectbox("Seat", [2,4,5,6,7,8,9,10])



model = pickle.load(open("car_pred", "rb"))


encode_dict = {{"fuel_type": {"Petrol": 0, "Diesel": 1, "CNG": 2},"transmission": {"Manual":1, "Automatic":2}}}


def model_pred(fuel_type, transmission_type, engine_power, seats):

    transmission_type = encode_dict["transmission"][transmission_type]
    fuel_type = encode_dict["fuel_type"][fuel_type]

    data = [[2018.0, 1, 40000, fuel_type, transmission_type, 18.0, engine_power, 85, seats]]

    return model.predict(data)

if st.button("Predict"):
    st.write(model_pred(fuel_type, transmission_type, Engine_power, seats))
else:
    st.write("Click on Predict, once you done with data")    

    