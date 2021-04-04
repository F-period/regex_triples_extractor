"""
数据预处理的模块
功能1：对输入数据的格式进行检测，如果不满足条件则进行报错
功能2：将template.json中的规则转换为{'属性':['正则1','正则2'...]}的格式
"""
import json
import sys

# 默认输入文件路径
template_path = "template.json"
source_data_path = "source_data.json"

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

# 读入json数据，并将它转化为字典{'属性1':['正则1','正则2'...], '属性2':'正则3'}
def process_template():
    try:
        template_file = open(template_path, "r", encoding="utf-8")
    except FileNotFoundError:
        print("ERROR: 请检查项目目录下模板定义文件template.json是否存在")
        sys.exit(0)
    except Exception:
        print("ERROR: 文件template.json打开失败")
    try:
        template_str_json = json.load(template_file, object_pairs_hook=my_obj_pairs_hook)
    except Exception:
        print("ERROR: template.json文件中包含JSON格式错误，请检查数据格式")
        sys.exit(0)
    return template_str_json

# 读入待处理数据，并将它转化为字典{'属性1':['正则1','正则2'...], '属性2':'正则3'}
def process_source_data():
    try:
        source_data_file = open(source_data_path, "r", encoding="utf-8")
    except FileNotFoundError:
        print("ERROR: 请检查项目目录下模板定义文件source_data.json是否存在")
        sys.exit(0)
    except Exception:
        print("ERROR: 文件source_data.json打开失败")
    try:
        source_data_json = json.load(source_data_file, object_pairs_hook=my_obj_pairs_hook)
    except Exception:
        print("ERROR: source_data.json文件中包含JSON格式错误，请检查数据格式")
        sys.exit(0)
    return source_data_json