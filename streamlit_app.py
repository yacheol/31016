import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 파일 업로드 또는 로컬 데이터 로딩
@st.cache_data
def load_data():
    df = pd.read_excel("KOBIS_역대_박스오피스_내역(공식통계_기준)_2025-06-05.xls")
    df.columns = df.columns.str.strip()  # 공백 제거
    return df

df = load_data()

st.title("🎬 국가별 영화 비율 분석 (KOBIS 박스오피스 데이터)")
st.markdown("영화진흥위원회 데이터 기반 국가별 영화 수/비율 시각화")

# 국가명 컬럼 추정 (예: '국적' 또는 '제작국가')
country_column = None
for col in df.columns:
    if "국" in col and ("국가" in col or "적" in col):
        country_column = col
        break

if country_column:
    country_counts = df[country_column].value_counts()
    country_ratio = (country_counts / country_counts.sum()) * 100

    st.subheader("📊 국가별 영화 수")
    st.bar_chart(country_counts)

    st.subheader("📈 국가별 영화 비율 (%)")
    fig, ax = plt.subplots()
    country_ratio.plot(kind="pie", autopct="%.1f%%", ax=ax, ylabel='')
    ax.set_title("국가별 비율")
    st.pyplot(fig)

    st.markdown("원하는 국가를 선택해서 개별 비율 확인할 수도 있어요.")
    selected_country = st.selectbox("국가 선택", country_counts.index)
    st.write(f"'{selected_country}'의 영화 수: {country_counts[selected_country]}편")
    st.write(f"전체 대비 비율: {country_ratio[selected_country]:.2f}%")
else:
    st.error("❌ 국가 정보를 포함한 열(예: '제작국가', '국적')을 찾을 수 없습니다.")
