"""
Usage:
    输入要查询的火车类型（动车高铁特快快速直达）
    输入出发地、目的地、出发日期。
    查询结果以命令行形式自动呈现。

Examples：
    Please input the trainType you want to search :-dgz
    Please input the city you want leave :南京
    Please input the city you will arrive :北京
    Please input the date(Example:2017-09-27) :2018-03-01
Options:
    -h,--help 查看帮助
    -d        动车
    -g        高铁
    -k        快速
    -t        特快
    -z        直达
"""

import requests,json
from docopt import docopt
from prettytable import PrettyTable
from colorama import init,Fore
from stations import stations

trainOption = input('-d动车 -g高铁 -k快速 -t特快 -z直达,Please input the trainType you want to search :')
fromStation = input('Please input the city you want leave :')
toStation = input('Please input the city you will arrive :')
tripDate = input('Please input the date(Example:2017-09-27) :')

init()

class TrainsCollection:
    header = '车次 车站 时间 历时 商务座 特等座 一等 二等 高级软卧 软卧 硬卧 软座 硬座 无座 其他'.split()
    def __init__(self,available_trains,options):
        """查询到的火车班次集合
        :param available_trains: 一个列表，包含可获得的火车班次，
                                 每个火车班次是一个字典。
        :param options = options: 查询的选项，如高铁，动车，etc...
        """
        self.available_trains = available_trains
        self.options = options

    @property
    def trains(self):
        for item in self.available_trains:
            cm = item.split('|')
            train_no = cm[3]
            initial = train_no[0].lower()
            if not self.options or initial in self.options:
                train = [
                train_no,
                '\n'.join([Fore.GREEN + cm[6] + Fore.RESET,
                          Fore.RED + cm[7] + Fore.RESET]),
                '\n'.join([Fore.GREEN + cm[8] + Fore.RESET,
                          Fore.RED + cm[9] + Fore.RESET]),
                cm[10],
                cm[32],
                cm[25],
                cm[31],
                cm[30],
                cm[21],
                cm[23],
                cm[28],
                cm[24],
                cm[29],
                cm[26],
                cm[22]   ]
                yield train
                """cq = {}
                cq['station_train_code'] = cm[3]#火车编号K76、G1018等
                cq['start_station_name'] = cm[4]#始发站
                cq['end_station_name'] = cm[5]#终到站
                cq['from_station_name'] = cm[6]#上车站
                cq['to_station_name'] = cm[7]#下车站
                cq['start_time'] = cm[8]#发车时间
                cq['arrive_time'] = cm[9]#抵达时间
                cq['lishi'] = cm[10]#行程历时
                cq['gg_num'] = cm[20] if cm[20] else "--"
                cq['gr_num'] = cm[21] if cm[21] else "--"
                cq['qt_num'] = cm[22] if cm[22] else "--"
                cq['rw_num'] = cm[23] if cm[23] else "--"
                cq['rz_num'] = cm[24] if cm[24] else "--"
                cq['tz_num'] = cm[25] if cm[25] else "--"
                cq['wz_num'] = cm[26] if cm[26] else "--"
                cq['yb_num'] = cm[27] if cm[27] else "--"
                cq['yw_num'] = cm[28] if cm[28] else "--"
                cq['yz_num'] = cm[29] if cm[29] else "--"
                cq['ze_num'] = cm[30] if cm[30] else "--"
                cq['zy_num'] = cm[31] if cm[31] else "--"
                cq['swz_num'] = cm[32] if cm[32] else "--"
                """

    def pretty_print(self):
        pt = PrettyTable()
        pt._set_field_names(self.header)
        for train in self.trains:
            pt.add_row(train)
        print(pt)

def searchTrain():
    """Command-line interface"""
    headers = {
        "Cache-Control":"no-cache",
        "Connection": "keep-alive",
        "Cookie":"__NRF=74C05F8DA4A54BAD8FE8C1858576401F; JSESSIONID=7F000001F6317B0C83A920B23A62A0D64E27924D83; route=495c805987d0f5c8c84b14f60212447d; BIGipServerotn=602931722.64545.0000; BIGipServerpool_passport=200081930.50215.0000; _jc_save_fromStation=%u4E0A%u6D77%2CSHH; _jc_save_toStation=%u5357%u4EAC%2CNJH; _jc_save_fromDate=2017-07-20; _jc_save_toDate=2017-07-18; _jc_save_wfdc_flag=dc",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        }
    arguments = {
    'option':trainOption,
    'from':fromStation,
    'to':toStation,
    'date':tripDate
    }
    from_station = stations[arguments['from']]
    to_station = stations[arguments['to']]
    date = arguments['date']
    url = ('https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT').format(date,from_station,to_station)
    options = ''.join([item for item in arguments['option']])
    r = requests.get(url,headers = headers,verify=False)
    print(url)
    available_trains = r.json()['data']['result']
    TrainsCollection(available_trains,options).pretty_print()

if __name__ == '__main__':
    searchTrain()
