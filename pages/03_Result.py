import streamlit as st

st.set_page_config(page_title="분석 결론", page_icon="✅", layout="wide")
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

col1, col2 = st.columns([3, 4])  # Adjust the ratio as needed

# Place images in pairs in the first column
with col1:
    image_col1, image_col2 = st.columns(2)
    with image_col1:
        st.image("image/주거면적_산업면적.png", use_column_width=True)
    with image_col2:
        st.image("image/유형별_면적대비_아파트수.png", use_column_width=True)

    image_col3, image_col4 = st.columns(2)
    with image_col3:
        st.image("image/유형별_노후_아파트_비율.png", use_column_width=True)
    with image_col4:
        st.image("image/주차장확보율.png", use_column_width=True)

# Place the text in the second column
with col2:
    st.write(
        """
        ##### 가설 2: 혼합형 지역은 주거 지역, 일자리 등 다양한 용도로 사용될 수 있기에 전기차 충전기 사용량이 많을 것으로 예상되며, 우선적으로 전기차 충전기를 설치해야 한다.  
        
        혼합형 지역은 예상과 다르게 상업지역보다 상대적으로 주거지역의 비율이 훨씬 높다.  
        이에 따라, 아파트 중심으로 충전 인프라를 보급해야하지만, k-apt 정보를 토대로 혼합형 지역은 노후 아파트 비율이 높아 주차장 확보율이 낮아 현실적으로 설치가 어렵습니다.
        """
    )
st.write("---")
