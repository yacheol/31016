import streamlit as st
import pandas as pd

# 데이터 로딩 함수
@st.cache_data
def load_data():
    # 7번째와 8번째 줄을 헤더로 사용
    df = pd.read_excel("KOBIS_역대_박스오피스_내역_공식통계_기준__2025-06-05.xlsx", header=[6, 7])
    return df

# 데이터 불러오기
df = load_data()

st.title("🎬 영화별 관객 수 조회기")

# 사용자 입력
movie_title = st.text_input("영화 제목을 입력하세요:")

if movie_title:
    # 컬럼 존재 여부 확인
    movie_col = ('영화명', 'Unnamed: 1_level_1')  # 예: '영화명' 밑에 아무 값 없는 경우
    audience_col = ('관객수', '(S:서울 기준)')

    if movie_col not in df.columns or audience_col not in df.columns:
        st.error(f"다중 헤더 형식에서 '{movie_col}' 또는 '{audience_col}' 컬럼을 찾을 수 없습니다.")
        st.write("사용 가능한 컬럼 목록:", df.columns.tolist())
    else:
        # 영화명 부분 검색 (대소문자 무시)
        result = df[df[movie_col].str.contains(movie_title, case=False, na=False)]

        if not result.empty:
            st.subheader("조회 결과")
            for _, row in result.iterrows():
                title = row[movie_col]
                audience = int(row[audience_col])
                st.write(f"🎞 **{title}** → 👥 {audience:,}명 관람")
        else:
            st.warning(f"'{movie_title}'에 해당하는 영화가 없습니다.")
