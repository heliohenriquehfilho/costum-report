import dash
from dash import dcc, html, dash_table, Input, Output
import pandas as pd
import plotly.express as px
from datetime import date

today = date.today()

style = {
    "title_font_family":'Garamond',
    'legend_font_family':'Garamond',
    'legend_font_size':16,
    'hoverlabel_font_family':'Garamond',
    'hoverlabel_font_size':16,
    'font_family':'Garamond',
    'font_size':16,
    'font_color':'#488A99'}

df = px.data.gapminder().query("continent == 'Oceania'")

fig = px.line(df, x='year', y='lifeExp', color='country',
    color_discrete_map={
        "Australia": "blue",
        "New Zeland": "green"})
fig.update_layout(paper_bgcolor='white', plot_bgcolor='white')
fig.update_layout(style)

figs = px.scatter(df, x='year', y='lifeExp', color='country',
    color_discrete_map={
        "Australia": "blue",
        "New Zeland": "green"}, )
figs.update_layout(paper_bgcolor='white', plot_bgcolor='white')
figs.update_layout(style)

figh = px.histogram(df, x='year', y='lifeExp', color='country',
    color_discrete_map={
        "Australia": "blue",
        "New Zeland": "green"})
figh.update_layout(paper_bgcolor='white', plot_bgcolor='white')
figh.update_layout(style)

df2 = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.Div([
        html.Div([
            html.Img(src=app.get_asset_url('logoclarinho.png'), alt='Labsmart', className='image-logo')],
            className='company-logo'),
        html.H3(['Relatório personalizavel com gráficos e tabelas.'], className='title', id='title'),
        html.H4([today], className='date'),
        ], className='navbar'),

        html.Div([html.Div([
            html.H4(['Lorem Ipsum'], className='subtitle', id="sub1"),
            html.P(['   Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec eget libero euismod, consequat sapien ut faucibus tellus.',
            'Cras placerat ligula sit amet erat maximus, vitae tristique massa pulvinar. Mauris faucibus, libero',
            'eu faucibus ultrices, sapien purus volutpat diam, eget fringilla libero orci id nibh. Sed ut vestibulum ipsum. Nulla',
            'lorem neque, efficitur varius libero eu, imperdiet mattis metus. Quisque accumsan egestas risus a condimentum. Nullam',
            'commodo blandit est sed elementum. Sed non ex ut massa gravida semper sed ut sapien. In hac habitasse platea dictumst.']),
            html.Div(
                [html.H5(['Fonte: Plotly'], className="cit"),
                html.A(['Link'], href="https://www.kaggle.com/code/jhossain/explore-the-gapminder-dataset-with-plotly-express", className="cit")],
                className='citacao')], className='text', id='txt1'),
                html.Div([
                    dcc.Dropdown(['Gráfico de linha', 'Gráfico de disperção', 'Histograma'], 'Escolha o tipo de gráfico que você deseja ver', id='demo-dropdown'),
                    html.Div(id='graph', className='graph')
                    ],className='graph')
            ], className='first-box', id="first-box"),

        html.Div([
            html.Div(dash_table.DataTable(
                data=df2.to_dict('records'),
                columns=[{'id': c, 'name': c} for c in df2.columns],
                style_table={'overflowX': 'auto'},
                style_cell_conditional=[{
                    'if': {'column_id': c},
                    'textAlign': 'left', 'width':'20%'
                } for c in ['Date', 'Region']],
                style_data={
                    'color': 'black',
                    'backgroundColor': 'white'},
                style_data_conditional=[{
                    'if': {'row_index': 'odd'},
                    'backgroundColor': '#b8b9ba',}],
                style_header={
                    'backgroundColor': '#b8b9ba',
                    'color': 'black',
                    'fontWeight': 'bold'},
                style_cell={
                    'fontSize':17,
                    'font-family':'Garamond'}), className="table"),
            html.Div([
                    html.H4(['Lorem Ipsum'], className='subtitle', id="sub2"),
                    html.P(['   Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec eget libero euismod, consequat sapien ut faucibus tellus.',
                    'Cras placerat ligula sit amet erat maximus, vitae tristique massa pulvinar. Mauris faucibus, libero',
                    'eu faucibus ultrices, sapien purus volutpat diam, eget fringilla libero orci id nibh. Sed ut vestibulum ipsum. Nulla',
                    'lorem neque, efficitur varius libero eu, imperdiet mattis metus. Quisque accumsan egestas risus a condimentum. Nullam',
                    'commodo blandit est sed elementum. Sed non ex ut massa gravida semper sed ut sapien. In hac habitasse platea dictumst.']),
                    html.Div([
                        html.H5(['Fonte: Plotly'], className="cit"),
                        html.A(['Link'], href="https://raw.githubusercontent.com/plotly/datasets/master/solar.csv", className="cit")],
                        className='citacao'),
                ],className='text', id='txt2'),
        ], className='second-box', id='second-box'),

        html.Div([
            html.H4(['Powered by:'], className='powered'),
            html.A(href='https://www.ifsc.edu.br/web/campus-florianopolis/pecce', children=[
                html.Img(src=app.get_asset_url('logo.png'), alt='PECCE', className='image')], className='logo'),
            html.Button('Baixar em PDF', id='run', className='btn')
            ], className='footer')

        ], className='outter-box-style', id='outter-box')

@app.callback(
    Output('graph', 'children'),
    Input('demo-dropdown', 'value')
)
def update_output(value):
    if value == "Gráfico de linha":
        return dcc.Graph(figure=fig, className='fig')
    elif value == "Gráfico de disperção":
        return dcc.Graph(figure=figs, className='fig')
    elif value == "Histograma":
        return dcc.Graph(figure=figh, className='fig')

if __name__ == '__main__':
    app.run_server(debug=True)
