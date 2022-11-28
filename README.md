# StreamlitNewsMap

<img width="417" alt="top_img01" src="https://user-images.githubusercontent.com/118791187/204228377-c13977ac-85e5-4484-a98d-d207b8f06855.PNG">

## 概要

Streamlit map機能の応用。ニュースAPIから地名を抽出して緯度経度に変換後、Streamlitのmapにプロットする。その際popupにリンク先を付与することで、元ニュース記事へのアクセスを簡略化した。

## 調査

1. ニュース記事を取得

→ どうにもうまくいかなさそうなので、RSS(もしくはTwitter)を使いましょう

[NHKニュースのRSS (okumuralab.org)](https://okumuralab.org/~okumura/python/nhkrss.html)

[RSS/RDFについて：朝日新聞デジタル (asahi.com)](https://www.asahi.com/information/service/rss.html)

[RSSについて | 毎日新聞 (mainichi.jp)](https://mainichi.jp/rss/)

[pythonでtwitter APIを利用してツイートを取得](https://python-man.club/python_twitter_api_tweet/#twitter_API)

 [](https://newsapi.org/)

1. ニュースの文字列から地名を取得 (NER/固有表現抽出という言語処理の分野)

[PyGeoNLP - Python版テキスト地名解析ツール | GeoNLP](https://geonlp.ex.nii.ac.jp/pygeonlp/)

→ うまくいかなさそう…市町村一覧と緯度経度リストを使う

[地方公共団体の位置データ Location Data of Local Governments in Japan](https://amano-tec.com/data/localgovernments.html)

1. 各市町村の緯度経度を取得

[国土地理院APIで住所から緯度・経度を取得](https://elsammit-beginnerblg.hatenablog.com/entry/2021/07/11/122916#%E5%9B%BD%E5%9C%9F%E5%9C%B0%E7%90%86%E9%99%A2API%E3%81%A7%E4%BD%8F%E6%89%80%E3%81%8B%E3%82%89%E7%B7%AF%E5%BA%A6%E7%B5%8C%E5%BA%A6%E3%82%92%E5%8F%96%E5%BE%97)

1. 地図にプロット (できればリンクを張り付けたい)

[folium 事始め - Qiita](https://qiita.com/pork_steak/items/f551fa09794831100faa)

[Folium Map: How to Create a Table-Style Pop-up with HTML Code](https://towardsdatascience.com/folium-map-how-to-create-a-table-style-pop-up-with-html-code-76903706b88a)

[Streamlitでstreamlit-foliumを使って地図に情報を表示してみよう](https://welovepython.net/streamlit-folium/)

## 結果

<img width="522" alt="img03" src="https://user-images.githubusercontent.com/118791187/204228414-b3cf46cb-d277-42b9-a7a5-0adbdfe55415.PNG">

<img width="417" alt="top_img01" src="https://user-images.githubusercontent.com/118791187/204228435-3120f0d8-1818-4ac2-82af-0e6105b5f6aa.PNG">

<img width="818" alt="top_img02" src="https://user-images.githubusercontent.com/118791187/204228458-a42a2bde-f5ac-4d63-8e68-b8030d9ce899.PNG">


## ディスカッション

・Twitterで追うのもできそう (読売, 朝日, 毎日…)

→ 今回はRSSからNHKの記事を拾ったが、Twitter APIから新聞等からも記事を拾うことができるか？

・今回は記事から地名を探索したが、BERTとかを使ってNER(固有表現抽出)の方法をとるか？

→ 要検討 ([リンク](https://www.intellilink.co.jp/column/ai/2022/022800.aspx))

・地名だけでなく、「皇居」「富士山」といったランドマークの緯度経度も取得したら？

→ 確かに。良いアイデア感謝 → [Google Maps Platform (****Places API****)を使う(有料)](https://developers.google.com/maps#:~:text=%E3%83%97%E3%83%AC%E3%82%A4%E3%82%B9-,Places%20API%20%E3%81%A8%20SDK,-Google%20%E3%81%8B%E3%82%89%E6%8F%90%E4%BE%9B)

・Streamlitとfolimを使っているけれど、Mapboxとか今風のGeoSDKを使わないの？

→ そう思ってMapboxのアカウント作ろうとしたら、クレカのZIPコード入力しなきゃいけなくて、そこで止まっている

・将来への展望は？

→ [こういったブログサイト](https://geo-news.jp/)で業界の現状を把握し、今後の企画を練る(できたら)
