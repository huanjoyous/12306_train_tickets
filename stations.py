import re
import requests
from pprint import pprint

url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9018'
response = requests.get(url,verify=False)
station = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)', response.text)
stations = dict(station)
with open('/users/zhaoluyang/小Python程序集合/12306_tickets/train_station_num.text','w') as file:
    file.write(response.text)
    file.close()
pprint(stations,indent = 4)
