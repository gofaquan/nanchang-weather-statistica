from spider.weather_spider import WeatherSpider


# 选择爬取的范围
def rangeTime(startYear=2020, startMonth=1, endYear=2022, endMonth=5):
    # 计算循环次数
    rangeNum = (endYear - startYear) * 12 + endMonth - startMonth + 1

    # 初始化一个spider，用于后续的数据读取
    spider = WeatherSpider(year=startYear, month=startMonth)

# 读取数据
    for i in range(rangeNum):
        # 输出当前读取的时间年月
        # print(spider.year, spider.month)

        # 读取数据
        weather_condition_dict, month_dict = spider.getData()

        # 返回数据到 generator 中
        yield weather_condition_dict, month_dict
