import dash
import pandas as pd
from dash import dcc, html, Input, Output
import plotly.graph_objects as go
import plotly.express as px
import dash_bootstrap_components as dbc

colors = {
    'bg': '#F5F5DC',
    'text': '#7FDBFF'
}

df = px.data.gapminder().query("continent == 'Oceania'")
fig = px.line(df, x='year', y='lifeExp', color='country')
fig.update_layout(paper_bgcolor=colors['bg'])

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv')

figs = go.Figure(data=[go.Table(
    header=dict(values=list(df.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[df.Rank, df.State, df.Postal, df.Population],
               fill_color='lavender',
               align='left'))
])
figs.update_layout(paper_bgcolor=colors['bg'])

app.layout = html.Div([
    html.H3(['Relatório personalizavel com gráficos e tabelas.'], style={'color':'#F8F8FF',
                                                                         'align-objects':'center',
                                                                         'display': 'flex',
                                                                         'flex-direction':'row',
                                                                         'align-objects':'center',
                                                                         'justify-content':'center',
                                                                         'width': '400',
                                                                         'font-size':'16',
                                                                         'text-align':'center',
                                                                                                'margin':'-8px',
                                                                                                'padding': '14px',
                                                                                                'border-style': 'solid',
                                                                                                'background-color': '#808080'}),
        html.Div([
            html.Div([
                    html.H4(['Lorem Ipsum']),
                    html.P(['   Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec eget libero euismod, consequat sapien ut faucibus tellus.',
                    'Cras placerat ligula sit amet erat maximus, vitae tristique massa pulvinar. Mauris faucibus, libero',
                    'eu faucibus ultrices, sapien purus volutpat diam, eget fringilla libero orci id nibh. Sed ut vestibulum ipsum. Nulla',
                    'lorem neque, efficitur varius libero eu, imperdiet mattis metus. Quisque accumsan egestas risus a condimentum. Nullam',
                    'commodo blandit est sed elementum. Sed non ex ut massa gravida semper sed ut sapien. In hac habitasse platea dictumst.']),
                    html.P(['Nunc porta purus ut neque rhoncus, nec varius nisi consequat. Donec euismod euismod finibus. Sed congue dignissim purus',
                    'sed pharetra. Suspendisse leo neque, pretium in placerat non, pellentesque at est. Nam quis erat imperdiet, sodales massa sed,',
                    'congue velit. Ut non consequat ante, quis ornare ipsum. Phasellus velit mi, scelerisque quis ante nec, gravida dictum.',
                    'Praesent laoreet, nisi a elementum placerat, erat magna congue erat, vitae accumsan ligula elit at metus. Donec neque purus,',
                    'convallis sed sapien eget, accumsan porta ipsum. Mauris convallis neque fermentum lacus malesuada suscipit. Nunc feugiat, ',
                    'diam id dignissim elementum, est sem elementum elit, vitae commodo nibh libero quis nisl. Aliquam porttitor nunc urna, ',
                    'quis tempus nulla fringilla ac. Donec in vulputate ex, at placerat libero. Etiam et auctor sem.'])
                ], style=  {'text-align': 'justify','text-justify': 'inter-word','background-color':'#F5F5DC',
                'padding':'5px', 'width':'50%', 'margin':'8px', 'heigh':'100px','text-indent': '50px'}),
            dcc.Graph(figure=fig, style={'padding':'5px','heigh':'50%', 'margin':'8px', 'width':'50%','background-color':'#F5F5DC'}),
        ], style={
            'display':'flex',
            'flex-direction':'row',
            'justify-content':'center',
            'align-content':'center',
            'background-color':'#F5F5DC',
            'margin':'-8px',
            'padding':'14px'
        }),
        html.Div([
            dcc.Graph(figure=figs, style={'padding':'5px','heigh':'3200px', 'margin':'8px'}),
            html.Div([
                    html.H4(['Lorem Ipsum']),
                    html.P(['   Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec eget libero euismod, consequat sapien ut faucibus tellus.',
                    'Cras placerat ligula sit amet erat maximus, vitae tristique massa pulvinar. Mauris faucibus, libero',
                    'eu faucibus ultrices, sapien purus volutpat diam, eget fringilla libero orci id nibh. Sed ut vestibulum ipsum. Nulla',
                    'lorem neque, efficitur varius libero eu, imperdiet mattis metus. Quisque accumsan egestas risus a condimentum. Nullam',
                    'commodo blandit est sed elementum. Sed non ex ut massa gravida semper sed ut sapien. In hac habitasse platea dictumst.']),
                    html.P(['Nunc porta purus ut neque rhoncus, nec varius nisi consequat. Donec euismod euismod finibus. Sed congue dignissim purus',
                    'sed pharetra. Suspendisse leo neque, pretium in placerat non, pellentesque at est. Nam quis erat imperdiet, sodales massa sed,',
                    'congue velit. Ut non consequat ante, quis ornare ipsum. Phasellus velit mi, scelerisque quis ante nec, gravida dictum.',
                    'Praesent laoreet, nisi a elementum placerat, erat magna congue erat, vitae accumsan ligula elit at metus. Donec neque purus,',
                    'convallis sed sapien eget, accumsan porta ipsum. Mauris convallis neque fermentum lacus malesuada suscipit. Nunc feugiat, ',
                    'diam id dignissim elementum, est sem elementum elit, vitae commodo nibh libero quis nisl. Aliquam porttitor nunc urna, ',
                    'quis tempus nulla fringilla ac. Donec in vulputate ex, at placerat libero. Etiam et auctor sem.'])
                ], style=  {'text-align': 'justify','text-justify': 'inter-word','background-color':'#F5F5DC',
                'padding':'5px', 'width':'50%', 'margin':'8px', 'heigh':'100px','text-indent': '50px'}),
        ], style={
            'display':'flex',
            'flex-direction':'row',
            'justify-content':'center',
            'align-content':'center',
            'background-color':'#F5F5DC',
            'margin':'-8px',
            'padding':'14px'
            }),
        html.Div([
            html.Img(
                src='http://labsmart.ifsc.edu.br/esplanada/img/labsmart-preto.png',
                style={
                    'height': '10%',
                    'width': '10%',
                    'padding-top' : 0,
                    'padding-right' : '10px',
                    'padding-left': '10px'},
                    ),

            html.A(['contato'], style={'color':'#F8F8FF','align-objects':'center',
            'align-objects':'center','justify-content':'center','text-align':'center','background-color': '#808080','margin-left':'40%','margin-top':'5px' ,'font-size':'14px'})

            ], style={'color':'#F8F8FF','align-objects':'left','display': 'flex','flex-direction':'row',
            'align-objects':'left','justify-content':'left','width': '400','text-align':'left',
            'margin':'-8px','padding': '14px','border-style': 'solid','background-color': '#808080'})

            ], style={'margin':0,'padding':0, 'background-color':'#F8F0E3'})

fig.write_image("images/fig1.pdf")
figs.write_image("images/fig1.pdf")

if __name__ == '__main__':
    app.run_server(debug=True)
