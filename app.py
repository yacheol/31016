import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.cluster import KMeans

st.title("배달 위치 군집 시각화")

# CSV 로드
df = pd.read_csv("Delivery.csv")

# 클러스터 수 입력
num_clusters = st.slider("군집 수를 선택하세요", min_value=2, max_value=10, value=3)

# KMeans 클러스터링 수행
coords = df[['Latitude', 'Longitude']]
kmeans = KMeans(n_clusters=num_clusters, random_state=0)
df['Cluster'] = kmeans.fit_predict(coords)

# 지도 시각화
st.subheader("군집 결과")
fig = px.scatter_mapbox(
    df,
    lat="Latitude",
    lon="Longitude",
    color="Cluster",
    hover_name="Num",
    zoom=10,
    height=600
)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

st.plotly_chart(fig)


