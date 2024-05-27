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
hide_streamlit_style = """
            <style>
            [data-testid="stToolbar"] {visibility: hidden !important;}
            footer {visibility: hidden !important;}
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

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


def _plot_occupancy_marker(row, map_element):
    lat = row["lat"]
    long = row["lng"]
    identify = row["station_charger_id"]
    address = row["address"]
    occupancy_rate = row["occupancy_rate"]

    if occupancy_rate < 30:
        color = "blue"
    elif occupancy_rate < 60:
        color = "green"
    elif occupancy_rate < 90:
        color = "orange"
    else:
        color = "red"

    folium.Marker(
        [lat, long],
        tooltip=identify,
        icon=folium.Icon(color=color),
        popup=f'<div style="width:300px">id : {identify}<br>address : {address}<br>Occupancy Rate: {occupancy_rate:.3f}%</div>',
    ).add_to(map_element)


def _plot_charging_rate_marker(row, map_element):
    lat = row["lat"]
    long = row["lng"]
    identify = row["station_charger_id"]
    address = row["address"]
    charging_rate = row["charging_rate"]

    if charging_rate < 30:
        color = "blue"
    elif charging_rate < 60:
        color = "green"
    elif charging_rate < 90:
        color = "orange"
    else:
        color = "red"

    folium.Marker(
        [lat, long],
        tooltip=identify,
        icon=folium.Icon(color=color),
        popup=f'<div style="width:300px">id : {identify}<br>address : {address}<br>Charging Rate: {charging_rate:.3f}%</div>',
    ).add_to(map_element)


@st.cache_data(show_spinner=True)
def create_occupancy_map(df):
    m = folium.Map(location=[37.5536067, 126.9674308], zoom_start=12)
    marker_cluster = MarkerCluster().add_to(m)
    heat_data = []

    for _, row in df.iterrows():
        _plot_occupancy_marker(row, marker_cluster)
        heat_data += [[row["lat"], row["lng"]]] * int(row["occupancy_rate"] / 30)

    HeatMap(heat_data).add_to(m)
    m.save(occupancy_html_path)


@st.cache_data(show_spinner=True)
def create_charging_rate_map(df):
    m = folium.Map(location=[37.5536067, 126.9674308], zoom_start=12)
    marker_cluster = MarkerCluster().add_to(m)
    heat_data = []

    for _, row in df.iterrows():
        _plot_charging_rate_marker(row, marker_cluster)
        heat_data += [[row["lat"], row["lng"]]] * int(row["charging_rate"] / 30)

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
