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
        
        혼합형 지역은 예상과 다르게 상업지역보다 상대적으로 주거지역의 비율이 훨씬 높습니다.  
        이에 따라, 아파트 중심으로 충전 인프라를 보급해야하지만, k-apt 정보를 토대로 혼합형 지역은 노후 아파트 비율이 높아 주차장 확보율이 낮아 현실적으로 설치가 어렵습니다.
        """
    )
st.write("---")


st.write(
    """
    ##### 최종 결론: 앞선 가설들을 바탕으로 경제활동을 중심으로 하는 주간형 지역에 충전 인프라를 설치해야 한다.
         """
)
st.write("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.image("image/직장인_선호도.png", use_column_width=True)
with col2:
    st.image("image/통행사슬.png", use_column_width=True)
with col3:
    st.image("image/통행사슬_종사자.png", use_column_width=True)

st.write(
    """
    - 서울시 내 승용차를 이용한 통행자를 대상으로 통행사슬 내 도착지점 유형을 직장, 학교, 기타로 구분해 **도착지점별 비중과 도착지에서의 평균 활동시간**을 분석한 결과 도착지점 유형 중 직장의 비중이 가장 높았습니다.
      - 승용차 이용 통행자 대부분이 직장인, 전기차의 잠재 수요층 역시 직장인이라는 것을 의미합니다.
    - 완속 충전기는 직장 및 학교 주차장, 즉, 장시간 머무르는 장소에서 수요가 많습니다.
      
      
    이를 기반으로 강남구에 전기차 충전 인프라를 보급할 것을 제안합니다.
    """
)
st.write("---")
st.image("image/아파트_회사_충전기현황.png", use_column_width=True)

st.write("""
         - 강남구는 IT 기업과 스타트업이 많이 모여 있으며, 서울특별시 지역내총생산 1위 지역입니다.  
         - 강남구는 아파트의 전기차 충전기의 개수와 점유율이 압도적으로 높습니다. 충전기 1대당 담당하는 전기차의 수가 가장 많은 자치구임에도 불구하고 여전히 충전기 공급이 부족합니다.  
         - 그에 비해, 직장의 충전기의 개수와 점유율을 적기 때문에 직장과 직장 근처에 충전기를 늘려서 수요를 해결해야 합니다.
         """)