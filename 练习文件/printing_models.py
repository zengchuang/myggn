'''
8-15 打印模型 ： 将示例print_models.py中的函数放在另一个名为printing_functions.py的文件中；
在print_models.py的开头编写一条import 语句， 并修改这个文件以使用导入的函数。
'''

import printing_functions as hello
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

hello.print_models(unprinted_designs, completed_models)
hello.show_completed_models(completed_models)


