import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

@st.cache_data
def load_data():
    try:
        df = pd.read_excel("KOBIS_역대_박스오피스_내역(공식통계_기준)_2025-06-05.xlsx", engine="openpyxl")
        df.columns = df.columns.str.strip()
        return df
    except Exception as e:
        st.error(f"파일 로드 중 오류 발생: {e}")
        return pd.DataFrame()  # 빈 데이터프레임 반환

df = load_data()

st.title("🎬 국가별 영화 비율 분석")
st.markdown("KOBIS 박스오피스 데이터를 기반으로 제작 국가 비율을 분석합니다.")

# '국가' 관련 열 자동 탐색
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

    selected = st.selectbox("🎯 특정 국가 선택", country_counts.index)
    st.write(f"**{selected}**: {country_counts[selected]}편 / {country_ratio[selected]:.2f}%")
else:
    st.error("❌ 국가 정보를 포함한 열(예: '제작국가', '국적')을 찾을 수 없습니다.")
