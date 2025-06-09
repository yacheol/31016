import streamlit as st
import pandas as pd

# 데이터 로딩 함수
@st.cache_data
def load_data():
    # 7번째 줄을 헤더로 사용해 불러오기
    df = pd.read_excel("KOBIS_역대_박스오피스_내역_공식통계_기준__2025-06-05.xlsx", header=6)
    return df

# 데이터 불러오기
df = load_data()

st.title("🎬 영화별 관객 수 조회기")

# 사용자 입력 받기
movie_title = st.text_input("영화 제목을 입력하세요:")

if movie_title:
    if '영화명' not in df.columns or '관객수 (S:서울 기준)' not in df.columns:
        st.error("'영화명' 또는 '관객수 (S:서울 기준)' 컬럼이 존재하지 않습니다.")
    else:
        # 영화명 부분 검색 (대소문자 무시)
        result = df[df['영화명'].str.contains(movie_title, case=False, na=False)]

        if not result.empty:
            st.subheader("조회 결과")
            for _, row in result.iterrows():
                title = row['영화명']
                audience = int(row['관객수 (S:서울 기준)'])
                st.write(f"🎞 **{title}** → 👥 {audience:,}명 관람")
        else:
            st.warning(f"'{movie_title}'에 해당하는 영화가 없습니다.")
