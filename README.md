# StreamlitNewsMap

<img width="417" alt="top_img01" src="https://user-images.githubusercontent.com/118791187/204228377-c13977ac-85e5-4484-a98d-d207b8f06855.PNG">

## 概要

Streamlit map機能の応用。NHKのRSSから記事を取得後、地名を抽出して緯度経度に変換してJSONに出力。そのJSONを読み込んで、Streamlitのmapにプロットする。popupにリンク先を付与することで、元ニュース記事へのアクセスを簡略化した。

## 実装

1. ニュース記事を取得

[NHKニュースのRSS (okumuralab.org)](https://okumuralab.org/~okumura/python/nhkrss.html)

[コピペで使える都道府県一覧リスト・県庁所在地一覧 (start-point.net)](https://www.start-point.net/maps/tool/)

2. 地方公共団体の緯度経度を取得

[地方公共団体の位置データ Location Data of Local Governments in Japan](https://amano-tec.com/data/localgovernments.html)

3. 地図にプロット(popupにリンクを付与)

[Streamlitでstreamlit-foliumを使って地図に情報を表示してみよう](https://welovepython.net/streamlit-folium/)

[folium 事始め - Qiita](https://qiita.com/pork_steak/items/f551fa09794831100faa)

[マーカーのPopupにWebページのリンクの貼り付け、TwitterやYouTubeなどを埋め込む - よちよちpython]https://chayarokurokuro.hatenablog.com/entry/2021/08/04/070359

## 結果

<img width="522" alt="img03" src="https://user-images.githubusercontent.com/118791187/204228414-b3cf46cb-d277-42b9-a7a5-0adbdfe55415.PNG">

<img width="417" alt="top_img01" src="https://user-images.githubusercontent.com/118791187/204228435-3120f0d8-1818-4ac2-82af-0e6105b5f6aa.PNG">

<img width="818" alt="top_img02" src="https://user-images.githubusercontent.com/118791187/204228458-a42a2bde-f5ac-4d63-8e68-b8030d9ce899.PNG">

↑記事へのジャンプ機能で[この記事](https://www3.nhk.or.jp/matsuyama-news/20221128/8000014600.html)へ移動

## ディスカッション

・今回は記事内容から地名を探索したが、BERTとかを使ってNER(固有表現抽出)の方法をとるか？

→ 要検討 ([リンク](https://www.intellilink.co.jp/column/ai/2022/022800.aspx))

・地名だけでなく、「皇居」「富士山」といったランドマークの緯度経度も取得したら？

→ 確かに。良いアイデア感謝 → [Google Maps Platform (****Places API****)を使う(有料)](https://developers.google.com/maps#:~:text=%E3%83%97%E3%83%AC%E3%82%A4%E3%82%B9-,Places%20API%20%E3%81%A8%20SDK,-Google%20%E3%81%8B%E3%82%89%E6%8F%90%E4%BE%9B)

・Streamlitとfolimを使っているけれど、Mapboxとか今風のGeoSDKを使わないの？

→ そう思ってMapboxのアカウント作ろうとしたら、クレカのZIPコード入力しなきゃいけなくて、そこで止まっている

・将来への展望は？

→ [こういったブログサイト](https://geo-news.jp/)で業界の現状を把握し、今後の企画を練る(できたら)
