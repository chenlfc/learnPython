import json

import pygal

from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS

from get_country_code_three_or_two import get_two_country_code as get_two

# 将数据加载到列表中
filename = './analysis_data/gdp_json.json'
years = range(1995, 2015)

with open(filename) as f:
    readers = json.load(f)
    # 处理获取的数据，获取指定年份里对应的国家代码及gdp数据
    for year in years:
        gdp_info = {}
        for reader in readers:
            if reader['Year'] == year:
                country_code = get_two(reader['Country Code'])
                value = int(float(reader['Value']))
                if country_code:
                    gdp_info[country_code.lower()] = value
                # else:
                #     print(reader['Country Code'], reader['Country Name'])

        # 根据gdp数据将所有国家分成三组
        gdp_pops_1, gdp_pops_2, gdp_pops_3 = {}, {}, {}
        for key, pop in gdp_info.items():
            if pop < 10000000000:
                gdp_pops_1[key] = pop
            elif pop < 100000000000:
                gdp_pops_2[key] = pop
            else:
                gdp_pops_3[key] = pop

        # 检查下总的分组国家和每个分组所包含的国家个数
        print(len(gdp_info), len(gdp_pops_1), len(gdp_pops_2), len(gdp_pops_3))

        # 根据gdp数据将图形化输出
        gm_style = RS('#336699', base_style=LCS)
        gm = pygal.maps.world.World(style=gm_style)

        gm.title = 'World GDP in ' + str(year) + ' by Country'
        gm.add('0-10bn', gdp_pops_1)
        gm.add('10bn-100bn', gdp_pops_2)
        gm.add('>100bn', gdp_pops_3)

        out_filename = './analysis_data/svg_files/gdp_world_' + str(
            year) + '.svg'
        gm.render_to_file(out_filename)
