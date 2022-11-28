import json
import random

#外部関数の読み込み
import sys
sys.path.append("./src")
from RssNHK import CollectNews
from GeoAPI import GetPrefAreaLatLong

#markerとpopup用のデータ作成
def ConstructPopup(dict_pref_articles, dict_pref_area_latlon):

    list_popup = []

    #県名の取得
    for pref in dict_pref_articles.keys():

        #各県の市町村区のリスト取得
        list_area = list(dict_pref_area_latlon[pref].keys())

        #記事リストの取得
        list_article = dict_pref_articles[pref]

        for article in list_article:
            title = article["title"]
            link  = article["link"]
            desc  = article["desc"]
        
            #市町村区の名前が記事にあれば
            is_serched = False
            for area in list_area[1:]:
                if area in title or area in desc:
                    lon_lat = dict_pref_area_latlon[pref][area]
                    print("{}{} : {}".format(area, lon_lat, title))
                    is_serched = True

                    list_popup.append({
                        "title" : title,
                        #"desc"  : desc,
                        "link"  : link,
                        "lat"   : lon_lat[0],
                        "lon"   : lon_lat[1],
                        "area"  : lon_lat[2]
                    })

                    #見つけたので次
                    break

            if not is_serched:
                area = list_area[0]
                lon_lat = dict_pref_area_latlon[pref][area]
                print("{}{} : {}".format(area, lon_lat, title))

                list_popup.append({
                    "title" : title,
                    #"desc"  : desc,
                    "link"  : link,
                    "lat"   : str(float(lon_lat[0]) + (random.random()/100)),
                    "lon"   : str(float(lon_lat[1]) + (random.random()/100)),
                    "area"  : lon_lat[2]
                })

        print("")

    return list_popup

def main():

    dict_pref_articles = CollectNews()

    dict_pref_area_latlon = GetPrefAreaLatLong()

    list_popup = ConstructPopup(dict_pref_articles, dict_pref_area_latlon)

    with open('./json/articles.json', mode="w") as f_json:
        json.dump(list_popup, f_json, indent=4, ensure_ascii=False) #JSON出力

if __name__ == '__main__':
    main()