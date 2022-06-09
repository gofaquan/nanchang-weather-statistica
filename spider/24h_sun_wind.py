import urllib.request, urllib.error
import bs4
import re
import pandas as pd


def flatten(List):
    return [item for sublist in List for item in sublist]


def main():
    baseurl = "https://www.tianqi.com/nanchang/"
    (
        wind_level,
        temperature,
        DataMap,
    ) = getData(baseurl)
    # 时间
    hours = DataMap[2] + DataMap[5] + DataMap[8] + DataMap[11]
    # 风力
    wind_level = flatten(wind_level)
    # 天气
    wheater = DataMap[0] + DataMap[3] + DataMap[6] + DataMap[9]
    # 风向
    wind = DataMap[1] + DataMap[4] + DataMap[7] + DataMap[10]

    flatten(hours)
    flatten(wind_level)
    # flatten(temperature)
    flatten(wheater)
    flatten(wind)

    spiderAns = pd.DataFrame(
        {
            "时间": hours,
            "风力": wind_level,
            "温度": temperature,
            "天气": wheater,
            "风向": wind,
        }
    )
    print(spiderAns)
    spiderAns.to_csv("charts/24h_sun_wind.csv", encoding="utf_8_sig")


findDate = re.compile(r'<dd class="week">(.*?)</dd>')  # 生成正则表达式，表示规则（字符串的模式）
findShidu = re.compile(r'<dd class="shidu"><b>(.*?)</b><b>(.*?)</b><b>(.*?)</b></dd>')
findkongqi = re.compile(
    r'<dd class="kongqi"><h5 style="background-color:(.*?)">(.*?)</h5><h6>(.*?)</h6><span>(.*?)<br/>(.*?)</span></dd>'
)
findNow = re.compile(r'<p class="now"><b>(.*?)</b><i>(.*?)</i></p>')
findNow1 = re.compile(r"<span><b>(.*?)</b>(.*?)</span>")
findw95 = re.compile(r'<li class="w95">(.*?)</li>')
findTem = re.compile(r"<span>(.*?)</span>")
findWind = re.compile(r'<li class="w95">(.*?)</li>')
findNum = re.compile(r'<li class="w95 mgtop5">(.*?)</li>')
findArea = re.compile(r'<a href="(.*)" title="(.*)">')
findTips = re.compile(
    r'<li><i><img src="(.*?)"/></i><b>(.*?)</b><a href="(.*?)"><p>(.*?)</p></a></li>'
)


# 爬取网页
def getData(baseurl):
    wind_level = []
    temperature = []
    DataMap = []

    html = askURL(baseurl)
    soup = bs4.BeautifulSoup(html, "html.parser")

    # 风力等级
    for level in soup.find_all("ul", class_="txt"):
        level = str(level)
        num = re.findall(findNum, level)
        if num:
            wind_level.append(num)

    # 温度
    for temp in soup.find_all("li", class_="w95"):
        temp = str(temp)
        tem = re.findall(findTem, temp)
        if tem:
            temperature.append(tem[0])

    # 风力和时间数据
    for item3 in soup.find_all("ul", class_="txt"):
        item3 = str(item3)
        wind = re.findall(findWind, item3)
        wind = tuple(wind)
        if wind:
            DataMap.append(wind)

    return wind_level, temperature, DataMap


def askURL(url):
    head = {
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
    request = urllib.request.Request(url, headers=head)  # 向网页提供请求
    html = ""
    # 异常处理
    try:
        response = urllib.request.urlopen(request)  # 请求打开网页
        html = response.read().decode("utf-8")  # 读取网页
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        elif hasattr(e, "reason"):
            print(e.reason)
    return html


if __name__ == "__main__":
    main()
