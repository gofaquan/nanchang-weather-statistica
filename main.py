from db.save_data import insert, read_month, read_day
from echarts.gen_chart import create_chart, calendar_day, pie_wind
from echarts.get_temperature import spilt_flag

if __name__ == "__main__":
    # insert(2021, 1, 2022, 4)
    # x, y1, y2, y3, y4 = read_month()
    # print(y1)
    #
    # create_chart(x, spilt_flag(y1), spilt_flag(y2), spilt_flag(y3), spilt_flag(y4))
    #
    # day_t = read_day()
    # print(spilt_flag(day_t))
    # calendar_day(spilt_flag(day_t))

    _, wind_data = read_day()
    pie_wind(wind_data)
