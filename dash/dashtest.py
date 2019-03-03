import dash
import dash_core_components as dcc 
import dash_html_components as html 

app = dash.Dash()

colors = {'background':'#111111','text':'#7fdbff'}

app.layout = html.Div(children=[
    html.H1('Hello dash!',style={'textAlign':'center',
                                'color':colors['text']}),
    html.Div('dash: web dsf'),
    dcc.Graph(id='example',figure={'data':[
        {'x':[1,2,3],'y':[4,1,2],'type':'bar','name':'SF'},
        {'x':[1,2,3],'y':[4,1,2],'type':'bar','name':'NYC'}
    ],
    'layout':{
        'title':'BAR PLOTS'
    }}),
    dcc.Graph(id='examp',figure={'data':[
        {'x':[1,234,3],'y':[4,15,25],'type':'line','name':'SadsF'},
        {'x':[1,24,345],'y':[425,1,2],'type':'line','name':'NYdasC'}
    ],
    'layout':{
        'plot_bgcolor':colors['background'],
        'title':'BARsd PLOTS',
        'paper_bgcolor':colors['background'],
        'font':{'color':colors['text']}
    }})
],style={'backgroundColor':colors['background']}
)

if __name__=='__main__':
    app.run_server()