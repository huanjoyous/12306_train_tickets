# 12306_train_tickets
Python实现12306火车票查询工具

"""Usage:
   tickets_my.py [-dgktz] <from> <to> <date>
   [-dgktz]:可选、如果不选，则默认查询所有类型的列车；
   <from>:出发地
   <to>:目的地
   <date>:出发时间，要求标准格式，如：2018-03-17
Options:
    -h,--help 查看帮助
    -d        动车
    -g        高铁
    -k        快速
    -t        特快
    -z        直达

Examples：
    tickets_my.py 上海 北京 2017-07-01
    tickets_my.py -dg 成都 南京 2017-07-01
"""
