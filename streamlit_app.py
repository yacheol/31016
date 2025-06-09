import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    df = pd.read_excel("KOBIS_역대_박스오피스_내역_공식통계_기준__2025-06-05.xlsx", header=[6, 7])
    df.columns = df.columns.map(lambda x: (str(x[0]).strip(), str(x[1]).strip()))  # 문자열화 + 공백 제거
    return df

df = load_data()

st.title("🎬 영화별 관객 수 조회기")

movie_col = ('영화명', '')  # 2단 헤더에서 하위가 빈 경우
aud_col = ('관객수', '(S:서울 기준)')

movie_name = st.text_input("영화 제목을 입력하세요:")

if movie_name:
    if movie_col not in df.columns or aud_col not in df.columns:
        st.error("컬럼명이 일치하지 않습니다. 실제 컬럼 목록:")
        st.write(df.columns.tolist())
    else:
        result = df[df[movie_col].str.contains(movie_name, case=False, na=False)]

        if not result.empty:
            st.subheader("조회 결과")
            for _, row in result.iterrows():
                title = row[movie_col]
                audience = int(row[aud_col])
                st.write(f"🎞 **{title}** → 👥 {audience:,}명 관람")
        else:
            st.warning(f"'{movie_name}'에 해당하는 영화를 찾을 수 없습니다.")
