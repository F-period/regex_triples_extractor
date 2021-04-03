"""
数据预处理的模块
功能1：对输入数据的格式进行检测，如果不满足条件则进行报错
功能2：将template.json中的规则转换为{'属性':['正则1','正则2'...]}的格式
"""
import json
import re

# 用于解决加载json数据时的重复键问题
# 将重复键对应的不同值结合形成一个列表
def my_obj_pairs_hook(lst):
    result = {}
    count = {}
    for key, val in lst:
        if key in count:
            count[key] = 1 + count[key]
        else:
            count[key]=1
        if key in result:
            if count[key] > 2:
                result[key].append(val)
            else:
                result[key] = [result[key], val]
        else:
            result[key] = val
    return result

# 读入json数据，并将它转化为字典{'属性':['正则1','正则2'...]}
def process_template():
    template_file = open("template.json", "r", encoding="utf-8")
    template_json = json.load(template_file, object_pairs_hook=my_obj_pairs_hook)
    return template_json
