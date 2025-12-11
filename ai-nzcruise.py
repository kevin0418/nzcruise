#
# NZ Cruise 20251124-10251204
#

import streamlit as st

# 페이지 설정 (배경색 등 추가 가능)
st.set_page_config(page_title="NZ 크루즈 여행 ", layout="wide")

# CSS 스타일 적용
st.markdown("""
<style>
    /* 버튼 색상 커스텀 */
    .stButton>button {
        background-color: #4CAF50;  /* 초록색 계열 */
        color: white;
        font-weight: bold;
        border: none;
        padding: 10px 24px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 8px;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #45a049;  /* 호버 시 색상 변경 */
    }
    
    /* 특정 버튼 별도 색상 지정 */
    #video-btn { background-color: #FF5722 !important; }  /* 주황색 */
    #talk-btn { background-color: #2196F3 !important; }   /* 파란색 */
    #ppt-btn { background-color: #9C27B0 !important; }     /* 보라색 */
    
    /* 강조 텍스트 스타일 */
    .highlight {
        font-weight: bold;
        color: #FF5722;  /* 주황색 */
    }
    .note {
        font-size: 14px;
        color: #666;
        font-style: italic;
    }
</style>
""", unsafe_allow_html=True)

# 타이틀
st.write("### AI 와 함께쓰는 크루주 여행기  ! 👋")

# 설명 텍스트 (bold 및 색상 적용)
st.markdown("""
<span class="highlight"> 멍때리기 위해 떠나는 여행,  내가 나한데 묻기위헤 떠나는 여행
            </span>  
여기 Kevin이 맛깔나게 풀어 줍니다.  
<span class="highlight">아래 4편을 의미 있게 보시길</span>  
""", unsafe_allow_html=True)

# # 대화 링크 버튼
st.link_button("대화 를 통해 듣기", "https://youtu.be/q4GkOITmr78")

# Video 링크 버튼
st.link_button("Video A 를 통해 보기", "https://youtu.be/C0HJxpCEnCM")

# Video 링크 버튼
st.link_button("Video B 를 통해 보기", "https://youtu.be/NBYnKCB5ZlQ")

# # PPT 링크 버튼
st.link_button("Video by Kevin 거 보기", "https://youtu.be/aKOkaElH_xc")
st.caption("화면이 안나오면 (zzz) 클릭하고 기다리면 됩니다, 1-2 분정도")






