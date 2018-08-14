# import json
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

# 将API响应存储在一个变量中
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

# 探索有关仓库的信息
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))

# 研究第一个仓库
# repo_dict = repo_dicts[0]
# info_lists = []
names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    # stars.append(repo_dict['stargazers_count'])
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': str(repo_dict['description']),
        'xlink': repo_dict['html_url'],
    }
    plot_dicts.append(plot_dict)
#     info_list = {}
#     # info_list['name'] = repo_dict['name']
#     # info_list['owner'] = repo_dict['owner']['login']
#     # info_list['stars'] = repo_dict['stargazers_count']
#     info_list['repository'] = repo_dict['html_url']
#     # info_list['created'] = repo_dict['created_at']
#     # info_list['updated'] = repo_dict['updated_at']
#     info_list['description'] = repo_dict['description']
#     info_lists.append(info_list)

# # 将数据写入JSON文件
# filename = './web_api/python_repos.json'
# with open(filename, 'w', encoding='utf-8') as f:
#     json.dump(info_lists, f, ensure_ascii=False)

# 可视化
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
# y_ls = []
# for y_l in range(0, 55001, 5000):
#     y_ls.append(y_l)
# my_config.y_labels = y_ls
my_config.truncate_label = 15
my_config.show_y_guides = True
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('./web_api/python_repos.svg')

# 输出所有的键
# print("\nKeys:", len(repo_dict))
# for key in sorted(repo_dict.keys()):
#     print(key)

# 处理结果
# print(response_dict.keys())
