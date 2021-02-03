from bokeh.plotting import figure, output_file, show
import pandas

df=pandas.read_csv("CriticalOrgAlarmReports(Debasish).csv",parse_dates=["Date"])
p=figure(width=400, height=400,y_axis_label="'number'",x_axis_label="'Datetime'",title="earth")
p.line(df["Date"],df["Close"],color="red",alpha=0.5)

output_file("Time_Series.html")
show(p)

