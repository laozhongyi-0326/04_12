# _*_ coding:utf-8 _*_
import requests
import json
import re

"""
	GET /mp/profile_ext?action=getmsg&__biz=MjM5MzMwNDQwNA==&f=json&offset=10&count=10&is_ok=1&scene=124&uin=777&key=777&pass_ticket=5Ux4XNvNb8tq5IpK8J%2BZPOSh1CknWOP8D9%2FemE6EJorKCarp5azU6lSmm2wwYsTO&wxtoken=&appmsg_token=952_lbkFmtPQRi4vKy1yCV7k06Wbb0UGVvOGIOC_qA~~&x5=1&f=json HTTP/1.1
Host	mp.weixin.qq.com
Connection	keep-alive
X-Requested-With	XMLHttpRequest
User-Agent	Mozilla/5.0 (Linux; Android 8.0; DUK-AL20 Build/HUAWEIDUK-AL20; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043909 Mobile Safari/537.36 MicroMessenger/6.6.5.1280(0x26060536) NetType/WIFI Language/zh_CN
Accept	*/*
Referer	https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MjM5MzMwNDQwNA==&scene=124&devicetype=android-26&version=26060536&lang=zh_CN&nettype=WIFI&a8scene=3&pass_ticket=5Ux4XNvNb8tq5IpK8J%2BZPOSh1CknWOP8D9%2FemE6EJorKCarp5azU6lSmm2wwYsTO&wx_header=1
Accept-Encoding	gzip, deflate
Accept-Language	zh-CN,zh-CN;q=0.8,en-US;q=0.6
Cookie	pgv_info=ssid=s9137301340; pgv_pvid=3181512624; rewardsn=; wxtokenkey=777; wxuin=797842701; devicetype=android-26; version=26060536; lang=zh_CN; pass_ticket=5Ux4XNvNb8tq5IpK8J+ZPOSh1CknWOP8D9/emE6EJorKCarp5azU6lSmm2wwYsTO; wap_sid2=CI26uPwCElxxRzRkcG9PTXBDV0hEenNneWtjdW9wMENUUllLUFNab2ZzX1ZyWlBEZHQwU3JGMTRIVTFXTGdSY2hDY2FMdUFMV1ZvbExMNTMxbnIxOU5aZVBhVzd0N2dEQUFBfjCrqbzWBTgNQJVO
Q-UA2	QV=3&PL=ADR&PR=WX&PP=com.tencent.mm&PPVN=6.6.5&TBSVC=43603&CO=BK&COVC=043909&PB=GE&VE=GA&DE=PHONE&CHID=0&LCID=9422&MO= DUK-AL20 &RL=1440*2408&OS=8.0.0&API=26
Q-GUID	fc36938211b6cf1949166132117888cb
Q-Auth	31045b957cf33acf31e40be2f3e71c5217597676a9729f1b
"""
headers ={'Host': 'mp.weixin.qq.com',
          "Cookie":"pgv_info=ssid=s9137301340; pgv_pvid=3181512624; rewardsn=; wxtokenkey=777; wxuin=797842701; devicetype=android-26; version=26060536; lang=zh_CN; pass_ticket=5Ux4XNvNb8tq5IpK8J+ZPOSh1CknWOP8D9/emE6EJorKCarp5azU6lSmm2wwYsTO; wap_sid2=CI26uPwCElxKd1FGVnBwMTVVNUFCdldUUW5mNWRXNG00cnl5eXpsRERFVE1WS0thNDhyQUp5R0JqTzIxQkRJbXdhY3EydTl5TUlRajJuYlBUQUtucDcyZ0ZsYjA1N2dEQUFBfjDSuLzWBTgNQJVO",
            "Q-UE2 QV":"QV=3&PL=ADR&PR=WX&PP=com.tencent.mm&PPVN=6.6.5&TBSVC=43603&CO=BK&COVC=043909&PB=GE&VE=GA&DE=PHONE&CHID=0&LCID=9422&MO= DUK-AL20 &RL=1440*2408&OS=8.0.0&API=26",
          "Q-GUID":"fc36938211b6cf1949166132117888cb",
          "Q-Auth":"31045b957cf33acf31e40be2f3e71c5217597676a9729f1b"
          }
# url ="http://mp.weixin.qq.com/mp/getmasssendmsg?__biz=MjM5MzMwNDQwNA==&wx_header=1"
# url ="https://mp.weixin.qq.com/mp/getappmsgext?__biz=MzA4OTEwNTUxNQ==&appmsg_type=9&mid=2649704168&sn=4b502e2bd502d8fcd834d1b2e7819fce&idx=1&scene=38&title=%E9%83%91%E5%B7%9E%E8%BD%A8%E9%81%93%E7%BA%BF%E7%BD%91%E6%80%BB%E5%AE%A2%E8%BF%90%E9%87%8F%E7%AA%81%E7%A0%B46%E4%BA%BF%E4%BA%BA%E6%AC%A1&ct=1522817710&abtest_cookie=BQABAAgACgALAAwADQAJAJ+GHgCVih4Ap4oeAD6LHgBKix4Ad4seAJaMHgDPjB4AA40eAAAA&devicetype=android-26&version=/mmbizwap/zh_CN/htmledition/js/appmsg/index3d0765.js&f=json&r=0.5396720909047206&is_need_ad=1&comment_id=221886057518596097&is_need_reward=0&both_ad=0&reward_uin_count=0&msg_daily_idx=1&is_original=0&uin=777&key=777&pass_ticket=5Ux4XNvNb8tq5IpK8J%25252BZPOSh1CknWOP8D9%25252FemE6EJorKCarp5azU6lSmm2wwYsTO&wxtoken=777&devicetype=android-26&clientversion=26060536&appmsg_token=952_xVUV9DzZHwjnURN28zY4TvHpCwhd7uBlcgFtmuvFUtkFL-dzg60n6uUJ6g9aTDg0-93PmfiiI0uD2XdU&x5=1&f=json"
url ="https://mp.weixin.qq.com/mp/profile_ext?action=getmsg&__biz=MjM5MzMwNDQwNA==&f=json&offset=10&count=10&is_ok=1&scene=124&uin=777&key=777&pass_ticket=5Ux4XNvNb8tq5IpK8J%2BZPOSh1CknWOP8D9%2FemE6EJorKCarp5azU6lSmm2wwYsTO&wxtoken=&appmsg_token=952_lbkFmtPQRi4vKy1yCV7k06Wbb0UGVvOGIOC_qA~~&x5=1&f=json"
# url ="https://mp.weixin.qq.com/mp/profile_ext?action=getmsg&__biz=MzIxNDQ5MzY0OQ==&f=json&offset=10&count=10&is_ok=1&scene=124&uin=777&key=777&pass_ticket=5Ux4XNvNb8tq5IpK8J%2BZPOSh1CknWOP8D9%2FemE6EJorKCarp5azU6lSmm2wwYsTO&wxtoken=&appmsg_token=952_tA9Mstygm6Lw%252FK1iTb8_t_FvRK481nrLOmB8uQ~~&x5=1&f=json"
response = requests.get(url,headers=headers)
res = response.content
# print res
json_str = json.loads(res)
msgs= json_str["general_msg_list"]
# print msgs
msg_re = re.search(r'({"list".*]})',msgs)
msg_str = msg_re.groups(0)[0]
msg_dict= json.loads(msg_str)
msg_list =  msg_dict['list']
for msg in msg_list:
    print msg

