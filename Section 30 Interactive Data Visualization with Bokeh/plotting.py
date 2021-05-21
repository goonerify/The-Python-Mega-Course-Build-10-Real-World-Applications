from bokeh.models import ColumnDataSource, HoverTool
from bokeh.plotting import figure, output_file, show

from motion_detector import df

df["Start_string"] = df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_string"] = df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")
print(df)

cds = ColumnDataSource(df)

p = figure(x_axis_type='datetime', height=100, width=500, sizing_mode="scale_width", title="Motion Graph")
p.yaxis.minor_tick_line_color = None
p.ygrid[0].ticker.desired_num_ticks = 1

hover = HoverTool(tooltips=[("Start","@Start_string"), ("End","@End_string")])
p.add_tools(hover)

q = p.quad(left="Start", right="End", bottom=0, top=1, color="green", source=cds)

output_file("Graph1.html")
show(p)
