from bokeh.plotting import figure, output_file, show
import pandas


df=pandas.DataFrame(columns=["X","Y"])
df["X"]=[1,2,3,4]
df["Y"]=[4,2,2,9]

p=figure(plot_width=400, plot_height=400,y_axis_label="'number'",x_axis_label="'count'",title="earth")
p.title.text="New earth"
p.xaxis.minor_tick_line_color='red'
p.yaxis.minor_tick_line_color=None
p.circle([1,2,3,4,5],[5,6,4,5,3],size=[i*5 for i in [5,6,4,5,3]],color="red",alpha=0.5)
output_file("scatter_plotting.html")
show(p)