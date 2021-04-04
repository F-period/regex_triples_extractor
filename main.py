"""
主函数
"""
import sys
from data_pre_process import process_template
from data_pre_process import process_source_data
from re_related_process import compile_regex_string
from re_related_process import extract_triple
from result_writer import output_extracted_triples


if __name__ == "__main__":
    # 前提：用户选定功能
    # 确保用户输入的参数数量和值都相等
    if len(sys.argv) != 2:
        print("ERROR: 请输入正确的命令(python main.py EXTRACT)")
        sys.exit(0)

    if sys.argv[1] == "EXTRACT":
        print("开始根据用户定义的模板对数据进行属性三元组抽取")
    else:
        print("ERROR: 请输入正确的命令(python main.py EXTRACT)")
        sys.exit(0)


    # 步骤一：解析用户定义的正则表达式模板
    template_str_json = process_template()
    template_json = compile_regex_string(template_str_json)

    # 步骤二：导入目标原数据
    source_data_json = process_source_data()

    # 步骤三: 抽取对应三元组
    triple_list = extract_triple(template_json, source_data_json)

    # 步骤四：输出文件
    output_extracted_triples(triple_list)

    print("任务已完成，很高兴你使用我的程序!")

