import pandas as pd
import plotly.offline as pyo
import plotly.figure_factory as ff
import plotly.graph_objs as go
import numpy as np

x=np.random.randn(200)
x2=np.random.randn(200)-2
x3=np.random.randn(200)+5


hist_data=[x,x2,x3]

group_labels = ['x1','x2','x3']

fig=ff.create_distplot(hist_data,group_labels,bin_size=[.2,.1,.4])
pyo.plot(fig,filename='histo.html')