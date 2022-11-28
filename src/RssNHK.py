import os
import csv
import feedparser

def CollectNews():

    cur_dir = os.path.dirname(os.path.abspath(__file__))
    path_csv = os.path.join(cur_dir, "csv/pref-city.csv")

    set_title = set()

    dict_pref_articles = {}

    def RSS(area, area_rome):

        list_article = []

        if area in ["東京", "大阪"]:
            return list_article

        rss  = "https://www3.nhk.or.jp/lnews/{}/toplist.xml".format(area_rome)

        d = feedparser.parse(rss)
        for i in d['entries']:
            title = i['title']
            desc  = i['description']
            link  = i['link']
            if title not in set_title:
                list_article.append({
                    "title": title,
                    "desc" : desc,
                    "link" : link})

                set_title.add(title)

        return list_article

    with open(path_csv, "r", encoding="ms932") as f:
        csvreader = csv.reader(f)
        for row in csvreader:
            area       = row[0]  # 県名
            area_roman = row[2]  # ローマ字
            list_article = RSS(area, area_roman)
            if len(list_article) > 0:
                dict_pref_articles[area] = list_article
                continue

            if row[0] == row[1]: # 県名と県庁所在地が一致するならスルー
                continue

            sub_area   = row[1] # 県庁所在地
            area_roman = row[3] # ローマ字
            list_article = RSS(sub_area, area_roman)
            if len(list_article) > 0:
                dict_pref_articles[area] = list_article

    return dict_pref_articles

def ToString():

    dict_pref_articles = CollectNews()

    for pref in dict_pref_articles.keys():
        print(pref)
        list_article = dict_pref_articles[pref]

        for article in list_article:
            title = article["title"]
            link  = article["link"]
            desc  = article["desc"][:40].replace('\n', ' ') + "..."

            print("    title : {}".format(title))
            print("    link  : {}".format(link))
            print("    desc  : {}".format(desc))
            print("")