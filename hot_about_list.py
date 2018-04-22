# _*_  coding:utf-8 _*_
import  requests
import json
import re

# url = "https://www.douyin.com/aweme/v1/aweme/post/?app_id=1128&max_cursor=0&count=7&user_id=85682668765"
url = "https://www.douyin.com/aweme/v1/aweme/post/?count=50&user_id=93025696966"
# url ="https://www.douyin.com/aweme/v1/aweme/post/?app_id=1128&max_cursor=0&count=36&user_id=61307122392"
# url = "https://www.douyin.com/aweme/v1/aweme/post/?app_id=1128&max_cursor=0&count=36&user_id=76891462174"
#
headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Mobile Safari/537.36"}

response = requests.get(url,headers=headers)
res = response.content
print res
# json_dict = json.loads(res)
# json_info_list = json_dict['aweme_list']
# print len(json_info_list)
# for json_info in json_info_list:
#     print json_info['statistics']
#     # print json_info['author']
#     pass