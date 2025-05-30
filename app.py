import streamlit as st
import pandas as pd
import plotly.express as px

# 제목
st.title("배달 위치 시각화")

# CSV 파일 로드
df = pd.read_csv("Delivery.csv")

# 데이터 확인
st.subheader("데이터 미리보기")
st.write(df.head())

# 지도 시각화
st.subheader("배달 위치 지도")
fig = px.scatter_mapbox(
    df,
    lat="Latitude",
    lon="Longitude",
    hover_name="Num",
    zoom=10,
    height=600
)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

st.plotly_chart(fig)
