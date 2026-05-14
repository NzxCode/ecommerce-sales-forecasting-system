
import streamlit as st
import numpy as np
import pickle

# load model
with open('sales_forecast_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title('AI Sales Forecast Dashboard')

day_index = st.slider(
    'Select Day Index',
    1,
    1000,
    100
)

prediction = (
    np.dot(
        np.array([[day_index]]),
        model['W']
    ) + model['B']
)

st.write(
    'Predicted Sales:',
    float(prediction[0][0])
)
