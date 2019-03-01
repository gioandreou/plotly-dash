import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df=pd.read_csv('Data/mpg.csv')

data = [go.Histogram(x=df['mpg'],xbins=dict(start=0,end=50,size=10))]
layout=go.Layout(title='Histogram')
fig = go.Figure(data=data,layout=layout)

#pyo.plot(fig,filename="histo.html")

df_exc =pd.read_csv('Data/abalone.csv')
data2 = [go.Histogram(x=df['length'],xbins=dict(start=0,end=1,size=0.02))]

layout2 = go.Layout(title='My histo')
fig2 = go.Figure(data=data2,layout=layout2)

pyo.plot(fig2,filename='histo_exc.html')