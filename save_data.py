import pymysql
from weather_spider import WeatherSpider

# 配置 mysql
db_config = {
    # IP
    "host": "127.0.0.1",
    # 端口
    "port": 3306,
    # 用户
    "user": "root",
    # 密码
    "passwd": "123456",
    # 要连接的数据库
    "database": "南昌天气",
    # 使用的字符集
    "charset": "utf8mb4",
}


# 数据插入表的函数
def insert_into_table_with_params(cu, table, params):
    keys = params.keys()
    values = params.values()
    sql = 'insert into {} ({}) values ("{}");'.format(table, ','.join(keys), '","'.join(values))
    print(sql)
    cu.execute(sql)


# 数据库连接初始化
def connectDB():
    # 连接 mysql
    conn = pymysql.connect(**db_config)
    cu = conn.cursor()

    return conn, cu


# 插入数据库
def insertData(cu, weatherSpider):
    # weatherSpider __init__  读取 dict 数据
    # 插入进 每月数据 表中
    insert_into_table_with_params(cu, '每月数据', weatherSpider.weather_condition_dict)

    # 迭代插入进 每日数据 表中
    for _, month_dict in weatherSpider.month_dict.items():
        insert_into_table_with_params(cu, '每日数据', month_dict)


# 提交插入的数据请求，完成插入
def commit(conn):
    conn.commit()
