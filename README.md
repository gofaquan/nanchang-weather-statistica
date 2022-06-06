### db

#### 插入

```python
# 数据插入表的函数
def insert_into_table_with_params(cu, table, params):
    keys = params.keys()
    values = params.values()
    sql = 'insert into {} ({}) values ("{}");'.format(table, ','.join(keys), '","'.join(values))
    # print(sql)
    cu.execute(sql)


# 插入数据库
def insertData(cu, weather_condition_dict, month_dict):
    # weatherSpider __init__  读取 dict 数据
    # 插入进 每月数据 表中
    insert_into_table_with_params(cu, '每月数据', weather_condition_dict)

    # 迭代插入进 每日数据 表中
    for _, month_dict in month_dict.items():
        insert_into_table_with_params(cu, '每日数据', month_dict)
```

#### 读取

```python
def read_month_data_2021(cu):
    date_sql = "select 日期 from 每月数据 where 日期 like '2021%';"
    //........
    

def read_day_data_2021(cu):
    sql = "select 最高温 from 每日数据 where 日期 like '2021%' ;"
	//.........

def read_day_wind_2021(cu):
    sql = "select 风力风向,count(*) from 每日数据 where 日期 like  '2021%' group by 风力风向;"
 	//............
```

#### 整合

```python
# 配置 mysql
db_config = {
    # IP
    "host": "127.0.0.1",
    //............
}
# 数据库连接初始化
def connectDB():


# 提交插入的数据请求，完成插入
def commit(conn):


# 将遍历的数据插入表
def insertRangeData(cu, startYear, startMonth, endYear, endMonth):
    # 最终插入函数，一步到位
def insert(startYear, startMonth, endYear, endMonth):
    # 获取 conn ,cu
    conn, cu = connectDB()
    //..........

def read_month():

def read_day():
```



### echarts

#### 图表生成代码

```python
def create_chart(x, y1, y2, y3, y4): #图表柱形图
    bar = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
            .add_xaxis(x)
            .add_yaxis("平均高温", y1)
            .add_yaxis("平均低温", y2)
     //.............

# 日历按每天 展示一年的数据
def calendar_day(data): 
    begin = datetime.date(2021, 1, 1)
    end = datetime.date(2021, 12, 31)
    data = [
        [str(begin + datetime.timedelta(days=i)), data[i]]
        for i in range((end - begin).days + 1)
        //..............
# 饼状图 ，展现每月的风力风向数据
def pie_wind(data):
		//............
```



### spider

#### 爬虫

```python
# em 标签对应该月指标数据
M = 'em'
# td 对应该月每天的指标数据
D = 'td'

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
		//............
        
                # 请求头
        self.headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
      			//.............
            
	   # 获取数据
    def getData(self):
        # 直接调用函数，数据载入两个 dict，之后可直接读取
        self.analyzeData(self.sendReq())

        # 时间逻辑判断
        if self.month == 12:
            # 爬取下一年
            self.month = 1
            self.year += 1
        else:
            # 爬取下一月
            self.month += 1
            //................
            
	    # 发送 GET 请求 获取 html
    def sendReq(self):
        # 设置请求参数  ?areaInfo[areaId]=58606&areaInfo[areaType]=2&date[year]=2020&date[month]=2
        param_dict = {
            'areaInfo[areaId]': self.areaId,
            'areaInfo[areaType]': self.areaType,
            'date[year]': self.year,
            'date[month]': self.month,
        }
            
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
            
      
            # 爬取日出日落，24h 每日天气等
//-------------------------------------------------------------------------------            
	 for item in soup.find_all('dd', class_='weather'):
        item = str(item)
        data = re.findall(findNow, item)[0]
        datalist7.append(data)
        data1 = re.findall(findNow1, item)[0]
        datalist7.append(data1)
        print(datalist7)
    for item1 in soup.find_all('ul', class_="txt"):
        # print(item1)
        item1 = str(item1)
        num = re.findall(findNum, item1)
        if num:
            datalist2.append(num)
    print(datalist2)
    for item2 in soup.find_all('li', class_="w95"):
        item2 = str(item2)
        tem = re.findall(findTem, item2)
        if tem:
            datalist3.append(tem[0])
    print(datalist3)
    data = []
    for item3 in soup.find_all('ul', class_="txt"):
        item3 = str(item3)
        wind = re.findall(findWind, item3)
        wind = tuple(wind)
        if wind:
            data.append(wind)

        if wind:
            datalist4.append(wind)            
```



