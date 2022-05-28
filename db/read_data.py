import pymysql


# 读取月度数据
def read_month_data(cu):
    date_sql = 'select 日期 from 每月数据;'
    a_t_sql = 'select 平均高温 from 每月数据;'
    a_b_sql = 'select 平均低温 from 每月数据;'

    cu.execute(date_sql)
    x_result = cu.fetchall()

    cu.execute(a_t_sql)
    a_t = list(cu.fetchall())

    cu.execute(a_b_sql)
    a_b = list(cu.fetchall())

    return x_result, a_t, a_b
