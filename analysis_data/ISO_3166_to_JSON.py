# 将ISO_3166-1的文件内容，根据表头转换为JSON格式并保存
import csv
import json

filename = './analysis_data/ISO_3166-1.csv'

with open(filename, encoding='utf-8') as f:
    all_nei_rong = csv.reader(f)
    title_nei_rong = next(all_nei_rong)

    iso_codes = []
    for infos in all_nei_rong:
        iso_code = {}
        iso_code['Two Code'] = infos[0]
        iso_code['Three Code'] = infos[1]
        iso_code['Number'] = infos[2]
        iso_code['ISO Code'] = infos[3]
        iso_code['Country Name (EN)'] = infos[4]
        iso_code['Country Name (CN)'] = infos[5]
        iso_codes.append(iso_code)

json_filename = './analysis_data/ISO_3166-1.json'
with open(json_filename, 'w', encoding='utf-8') as f:
    json.dump(iso_codes, f, ensure_ascii=False)
