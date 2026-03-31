import streamlit as st
import pickle
import numpy as np

# تحميل الموديل
model = pickle.load(open("model/model.pkl", "rb"))

st.title("🏠 House Price Prediction")

# إدخال المستخدم
area = st.number_input("Area (m²)", 20, 500)
rooms = st.number_input("Number of Rooms", 1, 10)
location = st.selectbox("Location", [1, 2, 3])

# زر التنبؤ
if st.button("Predict Price"):
    features = np.array([[area, rooms, location]])
    prediction = model.predict(features)
    st.success(f"Estimated Price: {int(prediction[0])} USD")