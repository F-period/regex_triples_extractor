"""
负责管理输出文件的模块
功能1：接受处理过程生成的结果，将它转换为输出文件
"""
import sys

# 默认输出文件路径
extracted_triple_path = "extracted_triple.txt"
labeled_data_path = "labeled_data.json"

# 默认的三元组分隔符
split_symbol = ";;;;"

# 接受抽取的结果列表[(实体,属性，属性值)]
# 将它转换为输出文件: 目录下的extracted_triple.txt
def output_extracted_triples(triple_list):
    if len(triple_list) == 0:
        print("WARNING: 没有在数据中抽取出三元组!")
        print("WARNING: 请重新检查数据是否正确，模板是否合理。")
        sys.exit(0)
    try:
        extracted_triple_output_file = open(extracted_triple_path, "w", encoding="utf-8")
    except Exception:
        print("ERROR: 三元组存储时IO发生错误")
    for triple in triple_list:
        line = triple[0] + split_symbol + triple[1] + split_symbol + triple[2] + '\n'
        extracted_triple_output_file.write(line)
    extracted_triple_output_file.close()
    print("三元组已经输入完毕，请查看文件目录下的extracted_triple.txt")
