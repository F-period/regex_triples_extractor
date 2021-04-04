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
        print("ERROR: 请输入正确的命令(python main.py EXTRACT|LABEL)")
        sys.exit(0)

    # FUNCTION_FLAG: 记录用户选择功能的标志量
    # =1时表示三元组抽取，=2时表示数据标注
    FUNCTION_FLAG = 0
    if sys.argv[1] == "EXTRACT":
        FUNCTION_FLAG = 1
        print("开始根据用户定义的模板对数据进行属性三元组抽取")
    elif sys.argv[1] == "LABEL":
        FUNCTION_FLAG = 2
        print("开始根据用户定义的模板对数据进行属性标注")
    else:
        print("ERROR: 请输入正确的命令(python main.py EXTRACT|LABEL)")
        print("TIPS:  其中EXTRACT表示三元组抽取，LABEL表示数据标注")
        sys.exit(0)


    # 步骤一：解析用户定义的正则表达式模板
    template_str_json = process_template()
    template_json = compile_regex_string(template_str_json)

    # 步骤二：导入目标原数据
    source_data_json = process_source_data()

    # 步骤三: 当FLAG=1时，抽取三元组
    if FUNCTION_FLAG == 1:
        triple_list = extract_triple(template_json, source_data_json)
        output_extracted_triples(triple_list)

    print("任务已完成，很高兴你使用我的程序!")

