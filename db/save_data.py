import pymysql
from db.insert_data import insertData
from db.read_data import read_month_data_2021,read_day_data_2021
from spider.range import rangeTime

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


# 数据库连接初始化
def connectDB():
    # 连接 mysql
    conn = pymysql.connect(**db_config)
    cu = conn.cursor()

    return conn, cu


# 提交插入的数据请求，完成插入
def commit(conn):
    conn.commit()


# 将遍历的数据插入表
def insertRangeData(cu, startYear, startMonth, endYear, endMonth):
    # 初始化一个 data generator
    data_generator = rangeTime(startYear, startMonth, endYear, endMonth)

    # 遍历里面的 dict 数据
    for weather_condition_dict, month_dict in data_generator:
        # 插入表中
        insertData(cu, weather_condition_dict, month_dict)


# 最终插入函数，一步到位
def insert(startYear, startMonth, endYear, endMonth):
    # 获取 conn ,cu
    conn, cu = connectDB()

    # 插入遍历数据
    insertRangeData(cu, startYear, startMonth, endYear, endMonth)

    # commit 数据请求
    commit(conn)


def read_month():
    # 获取 conn ,cu
    conn, cu = connectDB()

    result = read_month_data_2021(cu)

    # commit 数据请求
    commit(conn)

    return result


def read_day():
    # 获取 conn ,cu
    conn, cu = connectDB()

    result = read_day_data_2021(cu)

    # commit 数据请求
    commit(conn)

    return result
