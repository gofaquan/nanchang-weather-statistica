import pprint
import urllib.request, urllib.error
import requests
import bs4
import re
import xlwt
import sqlite3


def main():
    baseurl = "https://www.tianqi.com/nanchang/"
    # html = askURL(baseurl)
    #
    dbpath = "air.db"
    # getData(baseurl)
    datalist1, datalist2, datalist3, datalist4, datalist5, datalist6, datalist7 = getData(baseurl)
    # saveData2DB(datalist1, dbpath)
    # saveData2DB01(datalist2, datalist3, datalist4, datalist5, datalist6, datalist7, dbpath)
    print(datalist1)
    print(datalist2)
    print(datalist3)
    print(datalist4)
    print(datalist5)
    print(datalist6)
    print(datalist7)


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
    print(datalist1)
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

    print(datalist4)
    for item4 in soup.find_all('div', class_="mainWeather"):
        item4 = str(item4)
        area = re.findall(findArea, item4)
        datalist5 = area
    print(datalist5)
    for item5 in soup.find_all('div', class_="weather_life300"):
        # print(item5)
        item5 = str(item5)
        Tips = re.findall(findTips, item5)
        datalist6 = Tips
    print(datalist6)
    return datalist1, datalist2, datalist3, datalist4, datalist5, datalist6, datalist7




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


if __name__ == "__main__":
    main()
