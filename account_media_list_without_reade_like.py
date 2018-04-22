# _*_ coding:utf-8 _*_

import requests
import json
import re

a = 'var appuin ="MjM5MzMwNDQwNA=="||"";'
strs = a.find("var appuin =")+len("var appuin =")
end_index = a.find(";",strs)
saved_item = a[strs:end_index].replace('||', 'or')
bb = eval(saved_item)
print saved_item
print bb
# print end_index
# print strs