import streamlit as st
import pandas as pd

st.header("Task 2: 데이터 표시하기")
st.write("데이터프레임")

df= pd.read_csv("penguins.csv", encoding="utf-8")
st.dataframe(df)