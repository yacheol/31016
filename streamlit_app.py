import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 엑셀 파일 로딩
@st.cache_data
def load_data():
    df = pd.read_excel("KOBIS_역대_박스오피스_내역_공식통계_기준__2025-06-05.xlsx")
    return df

# 데이터 불러오기
df = load_data()

st.title("국가별 박스오피스 비율 조회")

# 사용자 입력 받기
country_input = st.text_input("국가명을 입력하세요 (예: 한국, 미국, 일본):")

if country_input:
    # '국적' 또는 유사한 컬럼명이 있어야 함
    if '국적' not in df.columns:
        st.error("'국적' 컬럼이 존재하지 않습니다. 데이터 파일 구조를 확인해주세요.")
    else:
        # 국가 기준 그룹화
        grouped = df.groupby('국적')['매출액'].sum()
        total_sales = grouped.sum()

        if country_input in grouped:
            country_sales = grouped[country_input]
            percentage = (country_sales / total_sales) * 100

            st.success(f"{country_input} 영화의 박스오피스 점유율: {percentage:.2f}%")

            # 파이 차트 시각화
            others_sales = total_sales - country_sales
            fig, ax = plt.subplots()
            ax.pie([country_sales, others_sales],
                   labels=[country_input, '기타 국가'],
                   autopct='%1.1f%%',
                   colors=['#4CAF50', '#CCCCCC'])
            st.pyplot(fig)
        else:
            st.warning(f"{country_input}에 해당하는 국적 정보가 없습니다.")

