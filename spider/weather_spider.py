import requests
import json
from bs4 import BeautifulSoup

# em 标签对应该月指标数据
M = 'em'

# td 对应该月每天的指标数据
D = 'td'


# 根据下标获取各类天气数据
def get_weather_data(obj, TYPE, index):
    return obj.findAll(TYPE)[index].text


# 定义天气爬虫类
class WeatherSpider:
    # 初始化
    def __init__(self, year=2020, month=1):
        # 地区 ID
        self.areaId = 58606
        # 地区类型
        self.areaType = 2
        # 查询年份
        self.year = year
        # 查询月份
        self.month = month

        # 查询的 url
        self.weather_url = 'http://tianqi.2345.com/Pc/GetHistory'

        # 指标数6个, 日期 最高温 最低温 天气 风力风向 空气质量指数
        self.QUOTA_NUM = 6

        # 存放单日指标
        self.day_condition_dict = {}
        # 存放当月每日指标
        self.month_dict = {}
        # 存放每月指标
        self.weather_condition_dict = {}

        # 请求头
        self.headers = {
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

    # 获取数据
    def getData(self):
        # 直接调用函数，数据载入两个 dict，之后可直接读取
        self.analyzeData(self.sendReq())

        # 时间逻辑判断
        if (self.month + 1) == 12:
            # 爬取下一年
            self.month = 1
            self.year += 1
        else:
            # 爬取下一月
            self.month += 1

        # 返回本次的数据
        return self.weather_condition_dict, self.month_dict

    # 发送 GET 请求 获取 html
    def sendReq(self):
        # 设置请求参数  ?areaInfo[areaId]=58606&areaInfo[areaType]=2&date[year]=2020&date[month]=2
        param_dict = {
            'areaInfo[areaId]': self.areaId,
            'areaInfo[areaType]': self.areaType,
            'date[year]': self.year,
            'date[month]': self.month,
        }

        # 发送 GET 请求获取 返回 json
        response = requests.get(url=self.weather_url, headers=self.headers, params=param_dict)

        # 接收 json
        resp_json = response.content.decode('gbk')

        # 载入 json
        resp_json = json.loads(resp_json)
        # 读取 json 内的 天气数据
        data = resp_json['data']

        # 输出数据查看
        # print(data)

        # 返回数据
        return data

    def analyzeData(self, data):
        # 解析 天气数据
        obj = BeautifulSoup(data, 'lxml')

        # 本月天数
        DAY = int(len(obj.findAll('td')) / self.QUOTA_NUM)

        # weather_condition_dict 载入数据
        self.fill_weather_data(obj, self.weather_condition_dict)

        # month_dict 载入 每日指标
        for i in range(DAY):  # 在当月天数的大小中依次添加

            self.fill_day_data(obj, self.day_condition_dict, i)  # day_condition_dict 载入数据
            self.month_dict[i + 1] = self.day_condition_dict  # month_dict 载入数据

            # 这里重新置为空! 如果不置为空则导致 数据都是当月最后一个数据
            self.day_condition_dict = {}

    # 将数据填入每月的 dict
    def fill_weather_data(self, obj, weather_dict):
        weather_dict['日期'] = str(self.year) + '年' + str(self.month) + '月'
        weather_dict['平均高温'] = get_weather_data(obj, M, 0)
        weather_dict['平均低温'] = get_weather_data(obj, M, 1)
        weather_dict['极端高温'] = get_weather_data(obj, M, 2)
        weather_dict['极端低温'] = get_weather_data(obj, M, 3)
        weather_dict['平均空气质量'] = get_weather_data(obj, M, 4)
        weather_dict['空气最好'] = get_weather_data(obj, M, 5)
        weather_dict['空气最差'] = get_weather_data(obj, M, 6)

    # 将数据填入每日的 dict
    def fill_day_data(self, obj, weather_dict, index):
        weather_dict['日期'] = get_weather_data(obj, D, index * self.QUOTA_NUM)
        weather_dict['最高温'] = get_weather_data(obj, D, index * self.QUOTA_NUM + 1)
        weather_dict['最低温'] = get_weather_data(obj, D, index * self.QUOTA_NUM + 2)
        weather_dict['天气'] = get_weather_data(obj, D, index * self.QUOTA_NUM + 3)
        weather_dict['风力风向'] = get_weather_data(obj, D, index * self.QUOTA_NUM + 4)
        weather_dict['空气质量指数'] = get_weather_data(obj, D, index * self.QUOTA_NUM + 5)

# a = WeatherSpider()
# # data = a.sendReq()
# # a.analyzeData(data)
# print(a.weather_condition_dict)
# print(a.month_dict)
# # # print(weather_condition_dict)
# # # print("====================================")
# # # print(month_dict)
