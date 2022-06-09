# 数据库air01
import sqlite3


def saveData2DB(datalist1, dbpath):
    init_db(dbpath)
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
    cur.execute('insert into air07(温度,天气,温度范围) values(?,?,?)', (str(datalist7[0][0])+str(datalist7[0][1]), datalist7[1][0], datalist7[1][1]))
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
