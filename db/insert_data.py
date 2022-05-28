import pymysql


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
