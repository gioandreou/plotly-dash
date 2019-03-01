import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('Data/2010YumaAZ.csv')
print(df)

days=['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']

data=[]

for day in days:
    trace= go.Scatter(x=df['LST_TIME'],
    y=df[df['DAY']==day]['T_HR_AVG'],
    mode='lines',
    name=day)

    data.append(trace)

layout = go.Layout(title='Daily temp avgs')

fig = go.Figure(data=data,layout=layout)
pyo.plot(fig,filename="line_exc.html")