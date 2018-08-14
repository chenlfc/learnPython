import requests
import json

from operator import itemgetter

# 执行API调用并存储响应
# url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

r = requests.get(url)
print("Status code:", r.status_code)

# 处理有关每篇文章的信息
submission_ids = r.json()

filename = './web_api/hn_submissions.json'
with open(filename, 'w') as f:
    js_read = []
    for submission_id in submission_ids['items']:
        js_read.append(submission_id)
        if js_read.__len__() == 30:
            json.dump(js_read, f)
            break
submission_dicts = []
# for submission_id in submission_ids[3]:
#     print(submission_id)
