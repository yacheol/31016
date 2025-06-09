import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 데이터 로딩 함수
@st.cache_data
def load_data():
    # 7번째 줄을 헤더로 사용하는 것이 핵심
    df = pd.read_excel("KOBIS_역대_박스오피스_내역_공식통계_기준__2025-06-05.xlsx", header=6)
    return df

# 데이터 불러오기
df = load_data()

st.title("국가별 박스오피스 점유율 분석")

# 사용자 입력 받기
country_input = st.text_input("국가명을 입력하세요 (예: 한국, 미국, 일본 등):")

# 유효한 입력일 때만 실행
if country_input:
    if '국적' not in df.columns or '매출액' not in df.columns:
        st.error("필요한 '국적' 또는 '매출액' 컬럼이 존재하지 않습니다.")
    else:
        # 결측값 제거
        df_filtered = df.dropna(subset=['국적', '매출액'])

        # 국가별 매출액 합산
        grouped = df_filtered.groupby('국적')['매출액'].sum()
        total_sales = grouped.sum()

        if country_input in grouped:
            country_sales = grouped[country_input]
            percentage = (country_sales / total_sales) * 100

            st.success(f"'{country_input}' 영화의 박스오피스 점유율은 {percentage:.2f}%입니다.")

            # 파이차트 시각화
            fig, ax = plt.subplots()
            ax.pie(
                [country_sales, total_sales - country_sales],
                labels=[country_input, '기타'],
                autopct='%1.1f%%',
                colors=['#ff9999', '#dddddd']
            )
            ax.set_title(f"{country_input} 영화 점유율")
            st.pyplot(fig)
        else:
            st.warning(f"'{country_input}'에 해당하는 영화 데이터가 없습니다.")

