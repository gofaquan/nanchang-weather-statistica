from spider import weather_spider
import save_data as db

if __name__ == "__main__":
    a = weather_spider.WeatherSpider()
    weather_condition_dict, month_dict = a.getData()

    # print(a.month_dict)
    conn, cu = db.connectDB()
    db.insertData(cu, a)

    db.commit(conn)
