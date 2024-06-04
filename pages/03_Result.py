import streamlit as st

st.set_page_config(page_title="상관관계 분석석", page_icon="📈", layout="wide")
hide_streamlit_style = """
            <style>
            [data-testid="stToolbar"] {visibility: hidden !important;}
            footer {visibility: hidden !important;}
                    body {
          margin: 0;
        }

        .wrapper {
          position: relative;
          z-index: 1;
          display: inline-block;
          width: 100vw;
        }

        .hidefooter {
          position: absolute;
          width: 150px;
          height: 35px;
          background: rgb(242,240,246);
          right: 0px;
          bottom: 0px;
          z-index: 2;
          display: block;
          color: rgb(0, 0, 0);
        }
    
        iframe {
          display: block;
          background: #ffffff;
          border: none;
          height: 99vh;
          width: 99vw;
        }
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# 컬럼 나누기
col1, col2 = st.columns([3, 4])
with col1:
    with st.container():
        st.image("image/파이차트.png", use_column_width=True)
        st.image("image/전기차보급확대정책.png", use_column_width=True)

with col2:
    with st.container():
        st.write(
            """
            ##### 가설 1: 인구 수, 소득, 사업용 전기차 수 등의 요인으로 경제 활동을 중심으로 하는 자치구에 전기차 충전기를 설치하는 것이 더 효율적  
            
            전기차 보급 확대 정책에 따라 기업들이 사업용 전기차를 늘리고 있는 추세로,
            주간형 지역은 사업용 전기차 비율이 상대적으로 높다는 것을 알 수 있습니다.
            이에 따라, 주간형 지역에 전기차 충전기를 설치하는 것이 타당합니다.
        """
        )

st.write("---")

col1, col2 = st.columns([3, 4])
with col1:
    with st.container():
        st.image("image/주거면적_산업면적.png", use_column_width=True)
        st.image("image/유형별_면적대비_아파트수.png", use_column_width=True)
        st.image("image/유형별_노후_아파트_비율.png", use_column_width=True)
        st.image("image/주차장확보율.png", use_column_width=True)

with col2:
    with st.container():
        st.write(
            """
            ##### 가설 1: 인구 수, 소득, 사업용 전기차 수 등의 요인으로 경제 활동을 중심으로 하는 자치구에 전기차 충전기를 설치하는 것이 더 효율적  
            
            전기차 보급 확대 정책에 따라 기업들이 사업용 전기차를 늘리고 있는 추세로,
            주간형 지역은 사업용 전기차 비율이 상대적으로 높다는 것을 알 수 있습니다.
            이에 따라, 주간형 지역에 전기차 충전기를 설치하는 것이 타당합니다.
        """
        )

st.write("---")
