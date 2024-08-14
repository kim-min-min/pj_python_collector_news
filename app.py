# 터미널: streamlit run ./app.py

# vscode github 연동

import streamlit as st

st.set_page_config(
    page_title="뉴스 수집기"
)

st.title("News : blue[Collector]")
st.text("Daum 뉴스를 수집합니다.")