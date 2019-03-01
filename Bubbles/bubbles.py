import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df=pd.read_csv("Data/mpg.csv")

data=[go.Scatter(x=df['horsepower'],
                y=df['mpg'],
                text=df['name'],
                mode='markers',
                marker=dict(size=df['weight']/100,
                showscale=True))]

layout = go.Layout(title='Bubble Chart',hovermode='x')
fig= go.Figure(data=data,layout=layout)
pyo.plot(fig,filename="bubbles.html")