"""
正则表达式匹配的专用模块
功能1：对模板字典的各字符串进行正则编译，如果不满足条件则进行报错
功能2：根据用户定义的正则在原数据中抽取符合的三元组
"""

import re

# 接受数据预处理模块转换后的字典
# 并且将它转换为字典{'属性1':[正则1，正则2...], ’属性2‘:正则3}
# 其中正则x是re库中的Pattern对象
def compile_regex_string(template_str_json):
    template_json = {}
    for key,value in template_str_json.items():
        if type(value).__name__ == "list":
            template_json[key] = []
            for each_str in value:
                try:
                    each_pattern = re.compile(each_str)
                except Exception:
                    print("编译正则表达式 "+key+":"+each_str+" 出错，请仔细检查正则表达式语法。")
                template_json[key].append(each_pattern)
        else:
            try:
                pattern = re.compile(value)
            except Exception:
                print("编译正则表达式 " + key + ":" + value + " 出错，请仔细检查正则表达式语法。")
            template_json[key] = pattern
    return template_json

# 根据用户定义的正则在原数据中抽取符合的三元组
# 接受编译后的正则字典以及原数据字典
# 返回抽取后的三元组结果列表[(实体,属性，属性值),...]
def extract_triple(template_json, source_data_json):
    triple_list = []
    for entity,text in source_data_json.items():
        for attribute,regex in template_json.items():
            attribute_value = []
            if type(regex).__name__ == "list":
                for each_regex in regex:
                    temp_result =  each_regex.findall(text)
                    attribute_value.extend(temp_result)
            else:
                attribute_value = regex.findall(text)
            if len(attribute_value) != 0:
                attribute_value = list(set(attribute_value))
                for value in attribute_value:
                    triple_list.append((entity, attribute, value))
    return triple_list
