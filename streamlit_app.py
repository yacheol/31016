# 필요한 라이브러리 불러오기
import streamlit as st               # Streamlit 앱 구축용
import pandas as pd                 # 데이터프레임 처리용
import matplotlib.pyplot as plt     # 시각화용
import matplotlib.font_manager as fm  # 폰트 설정용
import os                           # 파일 경로 확인용

# 📌 Streamlit Cloud에서 한글 폰트 설정
font_path = "/usr/share/fonts/truetype/nanum/NanumGothic.ttf"  # 나눔고딕 폰트 경로
if os.path.exists(font_path):  # 해당 경로에 폰트가 있으면
    font_name = fm.FontProperties(fname=font_path).get_name()  # 폰트 이름 추출
    plt.rc('font', family=font_name)  # matplotlib 기본 폰트 설정
    plt.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 깨짐 방지

# 🏠 웹 앱 제목과 설명 표시
st.title("🎬 국가별 영화 비율 분석")
st.markdown("KOBIS 박스오피스 데이터를 기반으로 제작 국가 비율을 분석합니다.")

# 📂 CSV 업로드 받기
uploaded_file = st.file_uploader("📂 CSV 파일 업로드", type=["csv"])

# ✅ 파일이 업로드되었을 때 처리
if uploaded_file is not None:
    try:
        # CSV 파일을 데이터프레임으로 읽기 (UTF-8 인코딩)
        df = pd.read_csv(uploaded_file, encoding="utf-8")
        df.columns = df.columns.str.strip()  # 열 이름의 공백 제거

        # 📌 '제작국가' 또는 '국적' 열 찾기
        country_column = None
        for col in df.columns:
            if "국" in col and ("국가" in col or "적" in col):  # ex. 제작국가, 국적 등
                country_column = col
                break

        # ✅ 제작국가 열이 존재할 경우
        if country_column:
            country_counts = df[country_column].value_counts()  # 국가별 영화 수 세기
            country_ratio = (country_counts / country_counts.sum()) * 100  # 비율 계산 (%)

            # 📊 막대그래프: 국가별 영화 수
            st.subheader("📊 국가별 영화 수")
            st.bar_chart(country_counts)

            # 🥧 원형 그래프: 국가별 비율
            st.subheader("📈 국가별 영화 비율 (%)")
            fig, ax = plt.subplots()
            country_ratio.plot(kind="pie", autopct="%.1f%%", ax=ax, ylabel='')  # 원형 차트
            ax.set_title("국가별 비율")
            st.pyplot(fig)  # Streamlit에 출력

            # ✅ 특정 국가 선택 시, 비율 및 개수 표시
            selected = st.selectbox("🎯 특정 국가 선택", country_counts.index)
            st.write(f"**{selected}**: {country_counts[selected]}편 / {country_ratio[selected]:.2f}%")

        else:
            # ❗ 제작국가 관련 열을 찾지 못한 경우
            st.warning("⚠️ '제작국가' 또는 '국적' 열을 찾을 수 없습니다.")

    except Exception as e:
        # ❌ 파일 처리 중 오류 발생 시
        st.error(f"❌ 파일 로드 오류: {e}")
else:
    # ℹ️ 파일이 아직 업로드되지 않은 경우
    st.info("ℹ️ 데이터를 불러오려면 CSV 파일을 업로드하세요.")


