import pymysql


# 读取月度数据
def read_month_data_2021(cu):
    date_sql = "select 日期 from 每月数据 where 日期 like '2021%';"
    a_t_sql = "select 平均高温 from 每月数据 where 日期 like '2021%';"
    t_sql = "select 极端高温 from 每月数据 where 日期 like '2021%' ;"
    a_b_sql = "select 平均低温 from 每月数据 where 日期 like '2021%' ;"
    b_sql = "select 极端低温 from 每月数据 where 日期 like '2021%' ;"

    cu.execute(date_sql)
    x_result = cu.fetchall()

    cu.execute(a_t_sql)
    a_t = list(cu.fetchall())

    cu.execute(a_b_sql)
    a_b = list(cu.fetchall())

    cu.execute(t_sql)
    t = list(cu.fetchall())

    cu.execute(b_sql)
    b = list(cu.fetchall())

    return x_result, a_t, a_b, t, b


def read_day_data_2021(cu):
    sql = "select 最高温 from 每日数据 where 日期 like '2021%' ;"
    cu.execute(sql)
    result = cu.fetchall()
    return result


def read_day_wind_2021(cu):
    sql = "select 风力风向,count(*) from 每日数据 where 日期 like  '2021%' group by 风力风向;"

    cu.execute(sql)
    result = cu.fetchall()
    return result
