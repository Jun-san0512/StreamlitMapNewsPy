import os
import csv

def GetPrefAreaLatLong():

    cur_dir  = os.path.dirname(os.path.abspath(__file__))
    path_csv = os.path.join(cur_dir, "csv/pref-lat-long.csv")

    dict_pref_area_latlon = {}

    with open(path_csv, "r", encoding="ms932") as f:
        csvreader = csv.reader(f)

        pref = ""
        for row in csvreader:

            if row[0][-1] in ["県", "都", "府"]:
                pref = row[0][:-1]
                dict_pref_area_latlon[pref] = {}
            elif row[0][-1] in ["道"]:
                pref = row[0]
                dict_pref_area_latlon[pref] = {}

            area = row[0]
            if area[-1] in ["都", "県", "府", "町", "村"]: #名前を削除
                area = area[:-1]
            elif area[-1] == "市" and area[-1] != pref: #市が県庁名と同じなら、削除しない
                area = area[:-1]

            dict_pref_area_latlon[pref][area] = (row[2], row[3], row[0])

    return dict_pref_area_latlon

"""---
def ToString():
    dict_pref_area_latlon = getPrefAreaLatLong()

    for pref in dict_pref_area_latlon.keys():
        print(pref)
        for area in dict_pref_area_latlon[pref].keys():
            tup_lon_lat_area = dict_pref_area_latlon[pref][area]
            print("    {} : {}".format(area, tup_lon_lat_area))

ToString()
#---"""