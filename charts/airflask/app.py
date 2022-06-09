from flask import Flask, render_template
import sqlite3
import spider2

spider2.main()
app = Flask(__name__)



@app.route('/')
def index():
    datalist = []
    conn = sqlite3.connect('air.db')
    cur = conn.cursor()
    sql = '''
    select * from air01,air07
    '''
    data = cur.execute(sql)
    # data1 = cur.execute('select * from air07')
    for item1 in data:
        datalist.append(item1)
    # for item in data1:
    #     datalist1.append(item)
    cur.close()
    conn.close()
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect('air.db')
    cur = conn.cursor()
    data1 = cur.execute('select 温度,时间 from air03,air04 where air03.序号=air04.序号 and air03.序号<13')
    for item in data1:
        datalist1.append(item[0])
        datalist2.append(item[1])
    cur.close()
    conn.close()
    datalist3 = []
    conn = sqlite3.connect('air.db')
    cur = conn.cursor()
    data2 = cur.execute('select 天气,时间,风向,风级 from air02,air04 where air02.序号=air04.序号')
    for item2 in data2:
        datalist3.append(item2)
    cur.close()
    conn.close()
    datalist4 = []
    datalist5 = []
    conn = sqlite3.connect('air.db')
    cur = conn.cursor()
    data3 = cur.execute('select 温度,时间 from air03,air04 where air03.序号=air04.序号 and 12<air03.序号')
    for item3 in data3:
        datalist4.append(item3[0])
        datalist5.append(item3[1])
    cur.close()
    conn.close()
    datalist6 = []
    conn = sqlite3.connect('air.db')
    cur = conn.cursor()
    data4 = cur.execute('select 链接,天气情况 from air05')
    for item4 in data4:
        datalist6.append(item4)
    cur.close()
    conn.close()
    datalist7 = []
    conn = sqlite3.connect('air.db')
    cur = conn.cursor()
    data5 = cur.execute('select 活动情况,网站,效果 from air06')
    for item5 in data5:
        datalist7.append(item5)
    return render_template('index.html', datalist=datalist, datalist1=datalist1, datalist2=datalist2,
                           datalist3=datalist3, datalist4=datalist4, datalist5=datalist5, datalist6=datalist6,
                           datalist7=datalist7)


@app.route('/index')
def home():
    return index()


@app.route('/May')
def may():
    datalist = []
    conn = sqlite3.connect('air.db')
    cur = conn.cursor()
    sql = '''
        select * from air01,air07
        '''
    data = cur.execute(sql)
    # data1 = cur.execute('select * from air07')
    for item1 in data:
        datalist.append(item1)
    # for item in data1:
    #     datalist1.append(item)
    cur.close()
    conn.close()
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect('air.db')
    cur = conn.cursor()
    data1 = cur.execute('select 温度,时间 from air03,air04 where air03.序号=air04.序号 and air03.序号<13')
    for item in data1:
        datalist1.append(item[0])
        datalist2.append(item[1])
    cur.close()
    conn.close()
    datalist3 = []
    conn = sqlite3.connect('air.db')
    cur = conn.cursor()
    data2 = cur.execute('select 天气,时间,风向,风级 from air02,air04 where air02.序号=air04.序号')
    for item2 in data2:
        datalist3.append(item2)
    cur.close()
    conn.close()
    datalist4 = []
    datalist5 = []
    conn = sqlite3.connect('air.db')
    cur = conn.cursor()
    data3 = cur.execute('select 温度,时间 from air03,air04 where air03.序号=air04.序号 and 12<air03.序号')
    for item3 in data3:
        datalist4.append(item3[0])
        datalist5.append(item3[1])
    cur.close()
    conn.close()
    datalist6 = []
    conn = sqlite3.connect('air.db')
    cur = conn.cursor()
    data4 = cur.execute('select * from monthweather1')
    for item4 in data4:
        datalist6.append(item4)
    cur.close()
    conn.close()
    return render_template('May.html', datalist=datalist, datalist1=datalist1, datalist2=datalist2,
                           datalist3=datalist3, datalist4=datalist4, datalist5=datalist5, datalist6=datalist6,
                           )


@app.route('/Team')
def team():
    return render_template('team.html')


@app.route('/air')
def air():
    datalist = []
    conn = sqlite3.connect('air.db')
    cur = conn.cursor()
    sql = '''
            select * from air01,air07
            '''
    data = cur.execute(sql)
    # data1 = cur.execute('select * from air07')
    for item1 in data:
        datalist.append(item1)
    # for item in data1:
    #     datalist1.append(item)
    dataList1 = str(datalist[0][6]).replace('PM:', '')
    print(dataList1)
    cur.close()
    conn.close()
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect('air.db')
    cur = conn.cursor()
    data1 = cur.execute('select 温度,时间 from air03,air04 where air03.序号=air04.序号 and air03.序号<13')
    for item in data1:
        datalist1.append(item[0])
        datalist2.append(item[1])
    cur.close()
    conn.close()
    datalist3 = []
    conn = sqlite3.connect('air.db')
    cur = conn.cursor()
    data2 = cur.execute('select 天气,时间,风向,风级 from air02,air04 where air02.序号=air04.序号')
    for item2 in data2:
        datalist3.append(item2)
    cur.close()
    conn.close()
    datalist4 = []
    datalist5 = []
    conn = sqlite3.connect('air.db')
    cur = conn.cursor()
    data3 = cur.execute('select 温度,时间 from air03,air04 where air03.序号=air04.序号 and 12<air03.序号')
    for item3 in data3:
        datalist4.append(item3[0])
        datalist5.append(item3[1])
    cur.close()
    conn.close()
    datalist6 = []
    conn = sqlite3.connect('air.db')
    cur = conn.cursor()
    data4 = cur.execute('select * from monthweather1')
    for item4 in data4:
        datalist6.append(item4)
    cur.close()
    conn.close()
    dataList3 = []
    conn = sqlite3.connect('air.db')
    cur = conn.cursor()
    data5 = cur.execute('select * from airpollutions')
    for item5 in data5:
        dataList3.append(item5)
    cur.close()
    conn.close()
    return render_template('air.html', datalist=datalist, datalist1=datalist1, datalist2=datalist2,
                           datalist3=datalist3, datalist4=datalist4, datalist5=datalist5, datalist6=datalist6,
                           dataList1=dataList1, dataList3=dataList3)


if __name__ == '__main__':
    app.run()
