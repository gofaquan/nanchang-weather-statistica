from pyecharts.charts import Bar
from pyecharts import options as opts
# 内置主题类型可查看 pyecharts.globals.ThemeType
from pyecharts.globals import ThemeType
import random
import datetime
from pyecharts.charts import Calendar

from pyecharts.charts import Pie


# 直方图
def create_chart(x, y1, y2, y3, y4):
    bar = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        .add_xaxis(x)
        .add_yaxis("平均高温", y1)
        .add_yaxis("平均低温", y2)
        .add_yaxis("最高温", y3)
        .add_yaxis("最低温", y4)
        .set_global_opts(title_opts=opts.TitleOpts(title="历年天气", subtitle="气温"),
                         xaxis_opts=opts.AxisOpts(
                             is_show=False,  # 隐藏X轴刻度
                         ), )
    )
    bar.render()


# 365天
def calendar_day(data):
    begin = datetime.date(2021, 1, 1)
    end = datetime.date(2021, 12, 31)
    data = [
        [str(begin + datetime.timedelta(days=i)), data[i]]
        for i in range((end - begin).days + 1)
    ]

    (
        Calendar(init_opts=opts.InitOpts(width="1600px", height="1000px"))
        .add(
            series_name="",
            yaxis_data=data,
            calendar_opts=opts.CalendarOpts(
                pos_top="120",
                pos_left="30",
                pos_right="30",
                range_="2021",
                yearlabel_opts=opts.CalendarYearLabelOpts(is_show=False),
            ),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(pos_top="30", pos_left="center", title="2021年最高温情况"),
            visualmap_opts=opts.VisualMapOpts(
                max_=45, min_=5, orient="horizontal", is_piecewise=False
            ),
        )
        .render("每日数据最高温.html")
    )


# 饼状图
def pie_wind(data):
    (
        Pie()
        .add("", data)
        .set_global_opts(title_opts=opts.TitleOpts(pos_top="50", pos_left="center", title="风力风向饼状图"))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
        .render("风力风向.html")
    )


# 仪表盘
def Gauge():
    (
        Gauge(init_opts=opts.InitOpts(width="1600px", height="800px"))
        .add(series_name="业务指标", data_pair=[["完成率", 55.5]])
        .set_global_opts(
            legend_opts=opts.LegendOpts(is_show=False),
            tooltip_opts=opts.TooltipOpts(is_show=True, formatter="{a} <br/>{b} : {c}%"),
        )
        .render("gauge.html")
    )


# 折线图
def Line():
    x = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期七', '星期日']
    y = [100, 200, 300, 400, 500, 400, 300]
    Line().set_global_opts(
        tooltip_opts=opts.TooltipOpts(is_show=False),
        xaxis_opts=opts.AxisOpts(type_="category"),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
    ).add_xaxis(xaxis_data=x).add_yaxis(
        series_name="基本折线图",
        y_axis=y,
        symbol="emptyCircle",
        is_symbol_show=True,
        label_opts=opts.LabelOpts(is_show=False),
    )
