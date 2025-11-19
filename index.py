import streamlit as st
import pandas as pd

st.header("Task 2: 데이터 표시하기")
st.write("데이터프레임")

df= pd.read_csv("penguins.csv", encoding="utf-8")
st.dataframe(df)

import streamlit as st
import pandas as pd


st.header("Task 3: 차트 그리기")
df= pd.read_csv("penguins.csv")
all_cols= df.columns.tolist()

st.markdown("""
    <style>
    h1, h2, h3, h4, h5, h6 {
        font-weight: 400 !important;  /* 일반 두께 */
    }
    </style>
""", unsafe_allow_html=True)
st.markdown("###### 📍모든 컬럼 목록")
st.markdown("\n".join([f"- **{col}**" for col in all_cols]))

selected_col= st.selectbox("그래프로 볼 컬럼을 선택하세요: ", all_cols)
st.markdown(f"###### > 선택된 칼럼: {selected_col}")

if pd.api.types.is_numeric_dtype(df[selected_col]):
    st.subheader("[선 그래프]")
    st.line_chart(df[selected_col])

    st.subheader("[막대 그래프]")
    st.bar_chart(df[selected_col])

    st.subheader("[영역 그래프]")
    st.area_chart(df[selected_col])

else:
    counts= df[selected_col].value_counts()

    st.subheader("[범주형 막대 그래프]")
    st.bar_chart(counts)