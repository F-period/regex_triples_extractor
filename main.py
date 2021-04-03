"""
主函数
"""

from data_pre_process import process_template

# template_json = process_template()
# print(template_json)

import sys


pattern = re.compile('\d{2}')
pattern.match('09计算机71软件工程91人工智能')
re.purge()