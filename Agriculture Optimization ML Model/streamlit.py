import os
import streamlit as st
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Dynamically find dataset file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data.xlsx")

@st.cache_resource
def load_and_train_model():
    data = pd.read_excel(DATA_PATH)
    y = data['label']
    X = data.drop(["label"], axis=1)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=0
    )
    lr = LogisticRegression(max_iter=1000)
    lr.fit(X_train, y_train)
    return lr

model = load_and_train_model()

def predict_crop(input_data):
    crop_label = model.predict(input_data)
    return crop_label[0]


def main():
    st.set_page_config(page_title="Agriculture Optimisation App", page_icon="🌱")
    st.title("🌱 Agriculture Optimisation App")
    st.write("Enter the environmental & soil parameters to predict the most suitable crop:")

    col1, col2 = st.columns(2)
    with col1:
        n = st.number_input("Nitrogen (N)", min_value=0.0, max_value=140.0, value=90.0)
        p = st.number_input("Phosphorus (P)", min_value=0.0, max_value=145.0, value=42.0)
        k = st.number_input("Potassium (K)", min_value=0.0, max_value=205.0, value=43.0)
        temperature = st.number_input("Temperature (°C)", min_value=0.0, max_value=60.0, value=20.8)
    with col2:
        humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=82.0)
        ph = st.number_input("pH level", min_value=0.0, max_value=14.0, value=6.5)
        rainfall = st.number_input("Rainfall (mm)", min_value=0.0, max_value=500.0, value=202.9)

    input_data = np.array([[n, p, k, temperature, humidity, ph, rainfall]])

    if st.button("Predict Recommended Crop"):
        crop_label = predict_crop(input_data)
        st.success(f"🌱 Recommended Crop: **{crop_label.upper()}**")


if __name__ == '__main__':
    main()

