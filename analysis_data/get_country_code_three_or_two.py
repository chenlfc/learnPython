import json


def get_two_country_code(three_code):
    """根据三位国家缩略码返回两位国家缩略码"""
    filename = './analysis_data/ISO_3166-1.json'
    with open(filename, encoding='utf-8') as f:
        readers = json.load(f)
        for reader in readers:
            # print(reader['Three Code'], reader['Two Code'])

            if reader['Three Code'] == three_code:
                return reader['Two Code']


def show_all_country_code():
    filename = './analysis_data/ISO_3166-1.json'
    with open(filename, encoding='utf-8') as f:
        readers = json.load(f)
        for reader in readers:
            print(reader['Two Code'] + ' ' + reader['Three Code'] + ' ' +
                  reader['Country Name (EN)'] + ' ' +
                  reader['Country Name (CN)'])
