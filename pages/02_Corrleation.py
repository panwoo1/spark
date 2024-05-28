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
col1, col2 = st.columns([2, 3])
with col1:
    with st.container():
        st.image("image/자치구_그룹핑.png", use_column_width=True)

with col2:
    with st.container():
        st.write(
            """
            ### 서울, 25개 자치구의 분류
            - 주간형: 오후 2시 peak  
            - 야간형: 오후 7시 peak  
            - 혼합형: 일자리, 주거지역 비율 유사, peak가 없고 분포가 비교적 균일  
            - 베드타운형: 아침, 저녁에 peak를 찍는 U자형 분포  
        """
        )

st.write("---")
import streamlit as st

col1, col2, col3 = st.columns(3)
with col1:
    st.image("image/충전기개수-사업체수.png", use_column_width=True)
with col2:
    st.image("image/충전기개수-아파트매매거래량.png", use_column_width=True)
with col3:
    st.image("image/충전기개수-전기차등록수.png", use_column_width=True)

col4, col5, lst = st.columns([1, 1, 1])
with col4:
    st.image("image/충전기개수-지가지수.png", use_column_width=True)
with col5:
    st.image("image/충전기개수-평당가.png", use_column_width=True)

st.markdown(
    """
**혼합형**: 전체적으로 왼쪽 아래에 분포하고 있습니다.  
**베드타운형**: 아웃라이어가 잘 없고, 추세선과 분포가 유사하거나 추세선 하단에 위치합니다.  
**주간형**: 아웃라이어가 많고(지자체 개수가 많음), 경제지구간의 특성은 주거지구의 특성에 비해 분포가 넓을 수밖에 없습니다.   
오른쪽에 위치하는 A형, 왼쪽에 위치하는 B형으로 두 가지 유형의 분포로 나눠서 볼 수 있습니다.
"""
)

st.write("---")
col1, col2 = st.columns([3, 4])
with col1:
    with st.container():
        st.image("image/충전기개수-아파트매매거래량.png", use_column_width=True)

with col2:
    with st.container():
        st.write(
            """
            #### 충전기 개수-아파트매매거래량
            1) **주간형**이 다른 그래프에서는 월등하게 높은 분포를 보였으나 아파트 매매거래량에서는 평균 혹은 이하의 분포를 보입니다.  
             ➡️ 경제 활동 지역이기 때문에 아파트 거래보다는 회사 등이 분포하는 것으로 보입니다.
              
            2) 노원구가 특히 높게 나온 이유는 신생아 특례대출과 GTX-C 노선 착공이 원인인 것으로 보입니다.  

        """
        )
st.write("---")
col1, col2 = st.columns([3, 4])
with col1:
    with st.container():
        st.image("image/충전기개수-지가지수.png", use_column_width=True)

with col2:
    with st.container():
        st.write(
            """
            #### 충전기 개수-지가지수
            1) 다른 지역에 비해 용산구의 지가지수가 높은 이유는 대통령 집무실 이전이 크게 기여했을 것으로 보입니다.
              
            2) 상관계수는 0.2619로 지가지수는 전기차 충전기 수에 큰 영향을 미치지 않는 것으로 보입니다.

        """
        )
st.write("---")
col1, col2 = st.columns([3, 4])
with col1:
    with st.container():
        st.image("image/충전기개수-사업체수.png", use_column_width=True)

with col2:
    with st.container():
        st.write(
            """
            #### 충전기 개수-사업체 수
            1) 분석한 그래프들 중 상관계수가 가장 높습니다.  
            ➡️ 전기차 충전기와 부동산 상관관계에서 다른 요인보다 사업체에서 전기차 충전기를 많이 이용하는 것으로 보입니다.  
              
                ➡️ 전기차 충전기는 주거 지역과 같은 다른 요인보다는 사업체와 연관이 많다는 판단을 하게 되었고, 이러한 양상을 보이는 원인에 초점을 맞춰 분석을 하였습니다.
            
        """
        )
st.write("---")
col1, col2 = st.columns([3, 4])
with col1:
    with st.container():
        st.image("image/충전기개수-전기차등록수.png", use_column_width=True)

with col2:
    with st.container():
        st.write(
            """
            #### 충전기 개수-전기차 등록 수

            - 당연하게도 전기차 등록수가 많은 지역에 전기차 충전기 개수가 많습니다. 상관관계도 두 변수는 강한 상관관계를 보여줍니다.  
            
            - 경제 지역 중 A유형에 전기차 등록수가 많은 것을 확인할 수 있습니다.  
            
            - 구로구가 다른 그래프에서는 높은 값을 보이지 않았는데, 전기차 등록수가 높게 나타난 이유는  
            구로구의 공무수행차들은 대부분 전기차를 이용합니다.  
            
            - 2022년 강남구 사업용 전기차 등록수는 10241대로 월등히 높습니다. 서초구는 비사업용 전기차 수가 강남구 다음으로 많습니다. 
            
        """
        )
st.write("---")
