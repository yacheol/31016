import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("🎬 국가별 영화 비율 분석")
st.markdown("KOBIS 박스오피스 데이터를 기반으로 제작 국가 비율을 분석합니다.")

uploaded_file = st.file_uploader("📂 CSV 파일 업로드", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file, encoding="utf-8")
        df.columns = df.columns.str.strip()

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
            st.warning("⚠️ '제작국가' 또는 '국적' 열을 찾을 수 없습니다.")
    except Exception as e:
        st.error(f"❌ 파일 로드 오류: {e}")
else:
    st.info("ℹ️ 데이터를 불러오려면 CSV 파일을 업로드하세요.")


