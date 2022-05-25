import requests
import json
from bs4 import BeautifulSoup

weather_url = 'http://tianqi.2345.com/Pc/GetHistory'

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    # 'Accept-Language': ' zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': 'Hm_lvt_a3f2879f6b3620a363bec646b7a8bcdd=1653402829,1653442456; Hm_lpvt_a3f2879f6b3620a363bec646b7a8bcdd=1653445895',
    'Host': 'tianqi.2345.com',
    'Referer': 'https://tianqi.2345.com/wea_history/58606.htm',
    # 'sec-ch-ua': ' " Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': "Windows",
    'Sec-Fetch-Dest': 'empty',
    # 'Sec-Fetch-Mode': ' cors',
    # 'Sec-Fetch-Site': ' same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

areaId = 58606
areaType = 2
year = 2020
month = 10
param_dict = {
    'areaInfo[areaId]': areaId,
    'areaInfo[areaType]': areaType,
    'date[year]': year,
    'date[month]': month,
}
# //?areaInfo[areaId]=58606&areaInfo[areaType]=2&date[year]=2020&date[month]=2

# 发送 GET 请求获取 返回 json
response = requests.get(url=weather_url, headers=headers, params=param_dict)
# 接收 json
resp_json = response.content.decode('gbk')
# 载入 json
resp_json = json.loads(resp_json)
# 读取 json 内的 天气数据
data = resp_json['data']

print(data)
# 解析 天气数据
weather_condition_dict = {}

obj = BeautifulSoup(data, 'lxml')

M = 'em'  # em 标签对应该月指标数据
D = 'td'  # td 对应该月每天的指标数据


# 根据下标获取各类天气数据
def get_weather_data(TYPE, index):
    return obj.findAll(TYPE)[index].text


# 将数据填入dict
def fill_weather_data():
    weather_condition_dict['avg_top_temperature'] = get_weather_data(M, 0)
    weather_condition_dict['avg_bot_temperature'] = get_weather_data(M, 1)
    weather_condition_dict['top_temperature'] = get_weather_data(M, 2)
    weather_condition_dict['bot_temperature'] = get_weather_data(M, 3)
    weather_condition_dict['avg_air_condition'] = get_weather_data(M, 4)
    weather_condition_dict['best_air_condition'] = get_weather_data(M, 5)
    weather_condition_dict['worse_air_condition'] = get_weather_data(M, 6)


fill_weather_data()
# print(weather_condition_dict)


QUOTA_NUM = 6  # 指标数6个, 日期 最高温 最低温 天气 风力风向 空气质量指数
DAY = int(len(obj.findAll('td')) / QUOTA_NUM)  # 本月天数

day_condition_dict = {}
month_dict = {}


def fill_day_data(index):
    day_condition_dict['最高温'] = get_weather_data(D, index * QUOTA_NUM + 1)
    day_condition_dict['最低温'] = get_weather_data(D, index * QUOTA_NUM + 2)
    day_condition_dict['天气'] = get_weather_data(D, index * QUOTA_NUM + 3)
    day_condition_dict['风力风向'] = get_weather_data(D, index * QUOTA_NUM + 4)
    day_condition_dict['空气质量指数'] = get_weather_data(D, index * QUOTA_NUM + 5)


for i in range(DAY):
    fill_day_data(i)
    month_dict[get_weather_data(D, i * 6)] = day_condition_dict

# print(month_dict)
for k1, v1 in month_dict.items():
    for k2, v2 in v1.items():
        print(k1, v2)
