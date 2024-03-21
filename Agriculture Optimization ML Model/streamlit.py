import streamlit as st
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
data = pd.read_excel(os.path.join(BASE_DIR, 'data.xlsx'))
y = data['label']
X = data.drop(["label"], axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
lr = LogisticRegression()
lr.fit(X_train, y_train)

def main():
    st.title("Agriculture Optimisation App")
    n = st.number_input("N", value=0.0)
    p = st.number_input("P", value=0.0)
    k = st.number_input("K", value=0.0)
    temperature = st.number_input("Temperature", value=0.0)
    humidity = st.number_input("Humidity", value=0.0)
    ph = st.number_input("pH", value=0.0)
    rainfall = st.number_input("Rainfall", value=0.0)
    if st.button("Predict"):
        crop = lr.predict([[n, p, k, temperature, humidity, ph, rainfall]])[0]
        st.write("Predicted Crop:", crop)

if __name__ == '__main__':
    main()
