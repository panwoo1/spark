import streamlit as st

st.set_page_config(
    page_title="Team Spark",
    page_icon="⚡",
)
hide_streamlit_style = """
            <style>
            [data-testid="stToolbar"] {visibility: hidden !important;}
            footer {visibility: hidden !important;}
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


st.markdown(
    """
# Team Spark
##### 전기차 충전기의 사용도 추정 및 부동산 상관관계 분석


"""
)
