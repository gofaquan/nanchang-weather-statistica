from spider import weather_spider
from spider.range import rangeTime
import save_data as db

if __name__ == "__main__":
    ret = rangeTime(2021, 3, 2021, 5)

    for a, b in ret:
        print(a)
        print(b)
    # print(weather_condition_dict)
    # print('-------------------------------------')
    # print(month_dict)
    # print('-------------------------------------')

    # # print(a.month_dict)
    # conn, cu = db.connectDB()
    # db.insertData(cu, weather_condition_dict,month_dict)
    #
    # db.commit(conn)
