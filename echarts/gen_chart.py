from pyecharts.charts import Bar
from pyecharts import options as opts
# 内置主题类型可查看 pyecharts.globals.ThemeType
from pyecharts.globals import ThemeType


def create_chart(x, y1, y2):
    bar = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
            .add_xaxis(x)
            .add_yaxis("平均高温", y1)
            .add_yaxis("平均低温", y2)
            .set_global_opts(title_opts=opts.TitleOpts(title="历年天气", subtitle="气温"))
    )
    bar.render()
