import dash
import dash_core_components as dcc 
import dash_html_components as html 
import plotly.graph_objs as go
import pandas as pd 

df = pd.read_csv('Data/OldFaithful.csv')

app = dash.Dash()

app.layout = html.Div([dcc.Graph(id='old_faithful',
                        figure={'data':[go.Scatter(x=df['X'],
                                                    y=df['Y'],
                                                    mode='markers')],
                                                    'layout':go.Layout(title='Old Faith',
                                                    xaxis={'title':'Duration'},
                                                    yaxis={'title':'interval'})}

) ])
if __name__ == '__main__':
    app.run_server()