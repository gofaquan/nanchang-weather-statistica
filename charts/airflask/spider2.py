import pprint
import urllib.request, urllib.error
import requests
import bs4
import re
import xlwt
import sqlite3


def main():
    month()
    pollution()
    baseurl = "https://www.tianqi.com/nanchang/"
    # html = askURL(baseurl)
    #
    dbpath = "air.db"
    # getData(baseurl)
    datalist1, datalist2, datalist3, datalist4, datalist5, datalist6, datalist7 = getData(baseurl)
    saveData2DB(datalist1, dbpath)
    saveData2DB01(datalist2, datalist3, datalist4, datalist5, datalist6, datalist7, dbpath)


# 影片详情规则
findDate = re.compile(r'<dd class="week">(.*?)</dd>')  # 生成正则表达式，表示规则（字符串的模式）
findShidu = re.compile(r'<dd class="shidu"><b>(.*?)</b><b>(.*?)</b><b>(.*?)</b></dd>')
findkongqi = re.compile(
    r'<dd class="kongqi"><h5 style="background-color:(.*?)">(.*?)</h5><h6>(.*?)</h6><span>(.*?)<br/>(.*?)</span></dd>')
findNow = re.compile(r'<p class="now"><b>(.*?)</b><i>(.*?)</i></p>')
findNow1 = re.compile(r'<span><b>(.*?)</b>(.*?)</span>')
findw95 = re.compile(
    r'<li class="w95">(.*?)</li>')
findTem = re.compile(r'<span>(.*?)</span>')
findWind = re.compile(r'<li class="w95">(.*?)</li>')
findNum = re.compile(r'<li class="w95 mgtop5">(.*?)</li>')
findArea = re.compile(r'<a href="(.*)" title="(.*)">')
findTips = re.compile(r'<li><i><img src="(.*?)"/></i><b>(.*?)</b><a href="(.*?)"><p>(.*?)</p></a></li>')


# findImasrc = re.compile(r'<img.*src="(.*?)"', re.S)  # re.S让换行符包含在字符中
# findTitle = re.compile(r'<span class="title">(.*)</span>')
# findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
# findJudge = re.compile(r'<span>(\d*)人评价</span>')
# findInq = re.compile(r'<span class="inq">(.*)</span>')
# findBd = re.compile(r'<p class="">(.*?) </p>', re.S)


# 爬取网页
def getData(baseurl):
    datalist1 = []
    datalist2 = []
    datalist3 = []
    datalist4 = []
    datalist5 = []
    datalist6 = []
    datalist7 = []
    html = askURL(baseurl)
    soup = bs4.BeautifulSoup(html, "html.parser")
    for item in soup.find_all('dl', class_="weather_info"):
        # print(item)
        item = str(item)
        Date = re.findall(findDate, item)[0]
        Shidu = re.findall(findShidu, item)[0]
        kongqi = re.findall(findkongqi, item)[0]
        datalist1.append(Date)
        for i in range(len(Shidu)):
            datalist1.append(Shidu[i])
        for i in range(len(kongqi)):
            datalist1.append(kongqi[i])
    for item in soup.find_all('dd', class_='weather'):
        item = str(item)
        data = re.findall(findNow, item)[0]
        datalist7.append(data)
        data1 = re.findall(findNow1, item)[0]
        datalist7.append(data1)
    for item1 in soup.find_all('ul', class_="txt"):
        # print(item1)
        item1 = str(item1)
        num = re.findall(findNum, item1)
        if num:
            datalist2.append(num)
    for item2 in soup.find_all('li', class_="w95"):
        item2 = str(item2)
        tem = re.findall(findTem, item2)
        if tem:
            datalist3.append(tem[0])
    data = []
    for item3 in soup.find_all('ul', class_="txt"):
        item3 = str(item3)
        wind = re.findall(findWind, item3)
        wind = tuple(wind)
        if wind:
            data.append(wind)

        if wind:
            datalist4.append(wind)

    for item4 in soup.find_all('div', class_="mainWeather"):
        item4 = str(item4)
        area = re.findall(findArea, item4)
        datalist5 = area
    for item5 in soup.find_all('div', class_="weather_life300"):
        # print(item5)
        item5 = str(item5)
        Tips = re.findall(findTips, item5)
        datalist6 = Tips
    return datalist1, datalist2, datalist3, datalist4, datalist5, datalist6, datalist7


# 数据库air01
def saveData2DB(datalist1, dbpath):
    # init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()
    sql1 = '''
       delete from air01;
       '''
    cur.execute(sql1)
    conn.commit()
    for index in range(len(datalist1)):
        datalist1[index] = '"' + datalist1[index] + '"'
    sql = '''
                insert into air01(
                日期,湿度,风向,紫外线,颜色,空气质量,PM,日出,日落
                )
            values(%s)
            ''' % ",".join(datalist1)
    # print(sql)
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()


def saveData2DB01(datalist2, datalist3, datalist4, datalist5, datalist6, datalist7, dbpath):
    # init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()

    sql1 = '''
           delete from air03;
           '''
    cur.execute(sql1)
    cur.execute('DELETE FROM sqlite_sequence')
    conn.commit()
    for j in range(24):
        sql2 = '''
                        insert into air03(
                        温度
                        )
                    values('%s');
                    ''' % "".join(datalist3[j])
        # print(sql)
        cur.execute(sql2)
    sql3 = '''
           delete from air02;
           '''
    cur.execute(sql3)
    cur.execute('DELETE FROM sqlite_sequence')
    conn.commit()
    for i in range(4):
        for j in range(6):
            sql = '''
                               insert into air02(
                               风级
                               )
                           values('%s');
                           ''' % "".join(datalist2[i][j])
            # print(sql)
            cur.execute(sql)
            conn.commit()
    sql4 = '''
               delete from air04;
               '''
    cur.execute(sql4)
    cur.execute('DELETE FROM sqlite_sequence')
    conn.commit()
    for j in range(4):
        for i in range(6):
            a = datalist4[0 + 3 * j][i]
            b = datalist4[1 + 3 * j][i]
            c = datalist4[2 + 3 * j][i]
            cur.execute('insert into air04(天气,风向,时间)values(?,?,?)', (a, b, c))
            conn.commit()
    sql5 = '''
                   delete from air05;
                   '''
    cur.execute(sql5)
    cur.execute('DELETE FROM sqlite_sequence')
    for data in datalist5:
        data = list(data)
        for index in range(len(data)):
            data[index] = '"' + data[index] + '"'
        sql6 = '''
                insert into air05(
                链接,天气情况
                )
            values(%s)
            ''' % ",".join(data)
        # print(sql)
        cur.execute(sql6)
        conn.commit()
    sql7 = '''
                       delete from air06;
                       '''
    cur.execute(sql7)
    cur.execute('DELETE FROM sqlite_sequence')
    for data in datalist6:
        data = list(data)
        for index in range(len(data)):
            data[index] = '"' + data[index] + '"'
        sql6 = '''
                    insert into air06(
                    图片链接,活动情况,网站,效果
                    )
                values(%s)
                ''' % ",".join(data)
        # print(sql)
        cur.execute(sql6)
        conn.commit()
    cur.execute('delete from air07')
    cur.execute('insert into air07(温度,天气,温度范围) values(?,?,?)',
                (str(datalist7[0][0]) + str(datalist7[0][1]), datalist7[1][0], datalist7[1][1]))
    conn.commit()
    cur.close()
    conn.close()


def init_db(dbpath):
    sql = '''
        create table air07
        (
            
            温度 int,
            天气 varchar(6),
            温度范围 varchar(20)
        );

    '''
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()


def save(dataList):
    dbpath = "air.db"
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()
    cur.execute('delete from monthweather1')
    conn.commit()
    sql = '''
    create  table if not exists monthweather1(日期 varchar(20) ,最高气温 varchar(20),
     最低气温 varchar (20), 天气 varchar (20),风向 varchar (20))
        '''
    cur.execute(sql)
    conn.commit()
    cur.execute('delete from monthweather1')
    conn.commit()
    for i in dataList:
        cur.execute('insert into monthweather1 values(?,?,?,?,?)', (i[0], i[1], i[2], i[3], i[4]))
    conn.commit()
    cur.close()
    conn.close()


def saveair(dataList):
    dbpath = "air.db"
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()
    cur.execute('delete from airpollutions')
    conn.commit()
    sql = '''
    create  table if not exists airpollutions(污染物名称 varchar(20) primary key ,浓度 varchar(20),
     等级 varchar (20))
        '''
    cur.execute(sql)
    for i in dataList:
        cur.execute('replace into airpollutions values(?,?,?)', (i[0], i[1], i[2]))
    conn.commit()
    cur.close()
    conn.close()


# for i in range(0, 10):  # 调用获取页面信息函数。10次
#     url = baseurl + str(i * 25)  # ?
#     html = askURL(url)  # 保存返回值
#     # 解析
#     soup = bs4.BeautifulSoup(html, "html.parser")
#     # 查找符合要求字符串
#     for item in soup.find_all('div', class_="item"):
#         # print(item)查看电影item
#         data = []  # 保存一部电影所以信息
#         item = str(item)
#         # print(item)
#         # break
#         # 获取到影片详情连接
#         link = re.findall(findLink, item)[0]  # re库用来通过正则表达式查找指定的字符串
#         data.append(link)
#         imgSrc = re.findall(findImasrc, item)[0]
#         data.append(imgSrc)
#         titles = re.findall(findTitle, item)
#         if len(titles) == 2:
#             ctitle = titles[0]
#             data.append(ctitle)
#             otitle = titles[1].replace("/", "")  # 去掉无关的符号
#             data.append(otitle)
#         else:
#             data.append(titles[0])
#             data.append(' ')  # 外国名留空
#
#         rating = re.findall(findRating, item)[0]
#         data.append(rating)
#         judgeNum = re.findall(findJudge, item)[0]
#         data.append(judgeNum)
#         inq = re.findall(findInq, item)
#         if len(inq) != 0:
#             inq = inq[0].replace("。", "")
#             data.append(inq)
#         else:
#             data.append(" ")
#         bd = re.findall(findBd, item)[0]
#         bd = re.sub('<br(\s+)?/>(\s+)', " ", bd)
#         bd = re.sub('/', " ", bd)  # 去/
#         data.append(bd.strip())  # 去掉空格
#         datalist.append(data)
# # print(datalist)
# return datalist


def askURL(url):
    head = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
    request = urllib.request.Request(url, headers=head)  # 向网页提供请求
    html = ""
    # 异常处理
    try:
        response = urllib.request.urlopen(request)  # 请求打开网页
        html = response.read().decode("utf-8")  # 读取网页
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        elif hasattr(e, "reason"):
            print(e.reason)
    return html


def pollution():
    url = "https://www.tianqi.com/air/nanchangxian.html"
    head = {"User-Agent": " Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                          " Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.54"}
    request = urllib.request.Request(url, headers=head)
    response = urllib.request.urlopen(request)
    html = response.read().decode("utf-8")
    soup = bs4.BeautifulSoup(html, "html.parser")
    findName = re.compile(r'<div class="pollute_item">(.*)</div>')
    findNumber = re.compile(r'<span>(.*)</span>')
    findGrade = re.compile(r'<span class="t\d">(.*)</span>')
    dataList3 = []
    for ite in soup.find_all('div', class_="air_pitem"):
        for item in ite.find_all('li'):
            data = []
            item = str(item)
            name = re.findall(findName, item)[0]
            data.append(name)
            number = re.findall(findNumber, item)[0]
            data.append(number)
            grade = re.findall(findGrade, item)[0]
            data.append(grade)
            dataList3.append(data)

    saveair(dataList3)


def month():
    url = "https://lishi.tianqi.com/nanchang/202205.html"
    head = {"User-Agent": " Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                          " Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.54"}
    request = urllib.request.Request(url, headers=head)
    response = urllib.request.urlopen(request)
    html = response.read().decode("utf-8")
    soup = bs4.BeautifulSoup(html, "html.parser")
    findDay = re.compile(r'<div class="th200">(.*)</div>')
    findother = re.compile(r'<div class="th140">(.*)</div>')
    dataList = []
    for ite in soup.find_all('ul', class_="thrui"):
        for item in ite.find_all('li'):
            data = []
            item = str(item)
            day = re.findall(findDay, item)[0]
            data.append(day)
            max = re.findall(findother, item)[0]
            data.append(max)
            min = re.findall(findother, item)[1]
            data.append(min)
            weather = re.findall(findother, item)[2]
            data.append(weather)
            wind = re.findall(findother, item)[3]
            data.append(wind)
            dataList.append(data)
    save(dataList)


if __name__ == "__main__":
    main()

