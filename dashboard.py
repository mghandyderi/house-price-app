import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data/house_data.csv")

st.title("📊 Data Dashboard")

st.write("Dataset Preview")
st.write(data)

st.write("Price Distribution")
plt.hist(data['Price'])
st.pyplot()

st.write("Area vs Price")
plt.scatter(data['Area'], data['Price'])
plt.xlabel("Area")
plt.ylabel("Price")
st.pyplot()