from db.save_data import insert, read_month
from echarts.gen_chart import create_chart
from echarts.get_temperature import spilt_flag

if __name__ == "__main__":
    # insert(2021, 1, 2022, 4)
    x, y1, y2 = read_month()
    print(y1)
    y1 = spilt_flag(y1)
    print(y1)
    # create_chart(x, y1, y2)

