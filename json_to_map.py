import json
import random

import pprint

import streamlit as st
import pandas as pd

import folium                          # folium(Leaflet.js)
from streamlit_folium import st_folium # streamlitでfoliumを使う
import branca                          # HTMLをfoliumのpopupに埋め込むのに使う

#地図に記事をプロットして表示
def ShowMap(list_popup):

    #地図の作成
    folium_map = folium.Map(
        location   = [36.381167, 138.767052],
        tiles='https://cyberjapandata.gsi.go.jp/xyz/std/{z}/{x}/{y}.png',
        attr='国土地理院',
        zoom_start = 5
    )

    #Markerにpopupを付与し、そこにHTMLを埋め込む
    for dict_article in list_popup:
        area  = dict_article["area"]
        title = dict_article["title"]
        link  = dict_article["link"]
        lat   = dict_article["lat"]
        lon   = dict_article["lon"]
        
        html = f'<p>{area}</p><a href={link} target="_blank" rel="noopener noreferrer"> {title} </a>'
        iframe = branca.element.IFrame(html=html, width=180, height=150)
        popup_html = folium.Popup(iframe, max_width=200, max_height=160)

        folium.Marker(
            location = [lat, lon], 
            popup    = popup_html
        ).add_to(folium_map)

    #地図の表示
    st_data = st_folium(folium_map, width=800, height=600)

def main():

    print("Update!")

    #json読み込んで、folimにプロット
    with open('./json/articles.json', 'r') as f_json:
        list_popup = json.load(f_json)

        #pprint.pprint(list_popup)

        ShowMap(list_popup)

if __name__ == '__main__':
    main()