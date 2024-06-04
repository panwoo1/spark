import os

import folium
import pandas as pd
import requests
import streamlit as st
import streamlit.components.v1 as components
from folium.plugins import HeatMap, MarkerCluster
from streamlit_folium import folium_static

st.set_page_config(
    page_title="전기차 충전기 점유율 히트맵", page_icon="🚗", layout="wide"
)
# hide_streamlit_style = """
#             <style>
#             [data-testid="stToolbar"] {visibility: hidden !important;}
#             footer {visibility: hidden !important;}
#             """
# st.markdown(hide_streamlit_style, unsafe_allow_html=True)

FASTAPI_URL = "http://127.0.0.1:8000/chargers/"
occupancy_html_path = "occupancy_heatmap.html"
charging_html_path = "charging_heatmap.html"


@st.cache_data(show_spinner=True)
def load_data():
    response = requests.get(FASTAPI_URL)
    response.raise_for_status()  # Ensure we notice bad responses
    data = response.json()
    df = pd.DataFrame(data)
    return df


@st.cache_data(show_spinner=True)
def create_occupancy_map(df):
    m = folium.Map(location=[37.5536067, 126.9674308], zoom_start=11)
    marker_cluster = MarkerCluster().add_to(m)

    # HeatMap 데이터 리스트
    heat_data = []

    for i in range(len(df)):
        lat = df.loc[i, "lat"]
        long = df.loc[i, "lng"]
        identify = df.loc[i, "station_charger_id"]
        address = df.loc[i, "address"]
        occupancy_rate = df.loc[i, "occupancy_rate"]

        # 사용률에 따른 마커 색상 결정
        if occupancy_rate < 30:
            color = "blue"
        elif occupancy_rate < 60:
            color = "green"
        elif occupancy_rate < 90:
            color = "orange"
        else:
            color = "red"

        # 마커 추가
        folium.Marker(
            [lat, long],
            tooltip=identify,
            icon=folium.Icon(color=color),
            popup=f'<div style="width:300px">id : {identify}</br>address : {address}</br>Occupancy Rate: {occupancy_rate:.3f}%</div>',
        ).add_to(marker_cluster)

        # HeatMap을 위해 각 위치를 사용률에 비례하여 여러 번 추가
        heat_data += [[lat, long]] * int(occupancy_rate / 50)

    # HeatMap 레이어 추가
    HeatMap(heat_data).add_to(m)
    m.save(occupancy_html_path)


@st.cache_data(show_spinner=True)
def create_charging_rate_map(df):
    m = folium.Map(location=[37.5536067, 126.9674308], zoom_start=11)
    marker_cluster = MarkerCluster().add_to(m)

    # HeatMap 데이터 리스트
    heat_data = []

    for i in range(len(df)):
        lat = df.loc[i, "lat"]
        long = df.loc[i, "lng"]
        identify = df.loc[i, "station_charger_id"]
        address = df.loc[i, "address"]
        charging_rate = df.loc[i, "charging_rate"]

        # 사용률에 따른 마커 색상 결정
        if charging_rate < 2730:
            color = "blue"
        elif charging_rate < 14927.5:
            color = "green"
        elif charging_rate < 38176.25:
            color = "orange"
        else:
            color = "red"

        # 마커 추가
        folium.Marker(
            [lat, long],
            tooltip=identify,
            icon=folium.Icon(color=color),
            popup=f'<div style="width:300px">id : {identify}</br>address : {address}</br>Occupancy Rate: {charging_rate:.3f}%</div>',
        ).add_to(marker_cluster)

        # HeatMap을 위해 각 위치를 사용률에 비례하여 여러 번 추가
        heat_data += [[lat, long]] * int(charging_rate / 120000)

    # HeatMap 레이어 추가
    HeatMap(heat_data).add_to(m)
    m.save(charging_html_path)


def load_heatmap(html_file):
    with open(html_file, "r", encoding="utf-8") as file:
        source_code = file.read()
    components.html(source_code, height=600, width=800)


def main():
    if not os.path.exists(occupancy_html_path) and not os.path.exists(
        charging_html_path
    ):
        df = load_data()
    # Generate and display occupancy heatmap
    if not os.path.exists(occupancy_html_path):
        create_occupancy_map(df)
    st.header("점유율 지도")
    load_heatmap(occupancy_html_path)

    # Generate and display charging heatmap
    if not os.path.exists(charging_html_path):
        create_charging_rate_map(df)
    st.header("충전량 지도")
    load_heatmap(charging_html_path)


if __name__ == "__main__":
    main()

# import streamlit as st
# import streamlit.components.v1 as components
# import utils as utl

# st.set_page_config(page_title="전기차 충전기 점유율 히트맵", page_icon="🚗")

# st.header("점유율 지도")
# with open("0513_map_with_heatmap.html", "r", encoding="utf-8") as HtmlFile:
#     source_code = HtmlFile.read()
#     components.html(source_code, height=600, width=800)

# st.header("충전량 지도")
# with open(
#     "0510_map_with_heatmap_charging_rate6.html", "r", encoding="utf-8"
# ) as HtmlFile:
#     source_code = HtmlFile.read()
#     components.html(source_code, height=600, width=800)
