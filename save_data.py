import pymysql

# 配置 mysql
db_config = {
    "host": "127.0.0.1",
    "user": "root",
    "passwd": "123456",
    "database": "南昌天气",
    "charset": "utf8mb4",
    "port": 3306
}


# 数据插入表
def insert_into_table_with_params(table, params):
    keys = params.keys()
    values = params.values()
    sql = 'insert into {} ({}) values ("{}");'.format(table, ','.join(keys), '","'.join(values))
    print(sql)
    cu.execute(sql)


# 连接 mysql
conn = pymysql.connect(**db_config)
cu = conn.cursor()
params = {
    '日期': '1',
    '最高温': '22°',
    '最低温': '17°',
    '天气': '阴',
    '风力风向': '东北风2级',
    '空气质量指数': '72 良'
}

insert_into_table_with_params('day_quota_data', params)

conn.commit()
