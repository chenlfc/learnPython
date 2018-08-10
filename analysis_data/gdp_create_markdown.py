years = range(1995, 2015)

gdp_md_filename = './analysis_data/gdp_world_show.md'
md_str = "# GDP数据处理后从1995-2015年的GDP地图\n\n"
md_str += "> ## The GDP World Maps\n\n"

for year in years:
    md_str += "  ![GDP_world_" + str(
        year) + ".svg](svg_files/gdp_world_" + str(year) + ".svg)\n"

with open(gdp_md_filename, 'w', encoding='utf-8') as f:
    f.writelines(md_str)
