# _*_ coding:utf-8 _*_
import requests
import json
import re

url ="https://api.amemv.com/aweme/v1/feed/?type=0&max_cursor=0&min_cursor=-1&count=6&volume=0.0&pull_type=2&need_relieve_aweme=0&ts=1523442128&app_type=normal&manifest_version_code=179&_rticket=1523442129052&ac=wifi&device_id=48180094693&iid=29426045083&os_version=8.0.0&channel=update&version_code=179&device_type=DUK-AL20&language=zh&uuid=865579035568614&resolution=1440*2408&openudid=7ffdb5c0b4777698&update_version_code=1792&app_name=aweme&version_name=1.7.9&os_api=26&device_brand=HONOR&ssmix=a&device_platform=android&dpi=640&aid=1128&as=a1e57e7cf08dda91dd4545&cp=e7dea35508d7c01be1dake&mas=00195a19685faac30d8c117f7f7f5a35d4ac2cac2c26268c9c8626"

# url ="https://api.amemv.com/aweme/v1/feed/?type=0&max_cursor=0&min_cursor=-1&count=6&volume=0.0&pull_type=2&need_relieve_aweme=0&ts=1523442384&app_type=normal&manifest_version_code=179&_rticket=1523442385008&ac=wifi&device_id=48180094693&iid=29426045083&os_version=8.0.0&channel=update&version_code=179&device_type=DUK-AL20&language=zh&uuid=865579035568614&resolution=1440*2408&openudid=7ffdb5c0b4777698&update_version_code=1792&app_name=aweme&version_name=1.7.9&os_api=26&device_brand=HONOR&ssmix=a&device_platform=android&dpi=640&aid=1128&as=a1251efc804d7a825d7564&cp=e5d4af5c01d0c321e1skxp&mas=000c846cf6f4e6330bc8b0cd5b408f10a62c6cacec26ac4c1c86ec"

response = requests.get(url)

res = response.content
print res