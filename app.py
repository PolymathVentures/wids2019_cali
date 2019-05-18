import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

df_earning = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/school_earnings.csv")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.P('Dash: A web application framework for Python.'),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    ),

    html.Label('Select Schools'),
    dcc.Dropdown(
        id="select-school",
        options=[{"label": s, "value": s} for s in df_earning.School],
        multi=True
    ),
    html.Label("Select range"),
    dcc.RangeSlider(
        id="gap-range",
        marks={i: str(i) for i in range(0, 100, 10)},
        min=0,
        max=100,
        value=[0, 100]
    ),

    html.Hr(),
    
    dcc.Graph(
        id="school-earnings",
        figure={
            'data': [
                {'x': df_earning.School, 'y': df_earning.Gap, 'type': 'bar'}
            ]
        }
    ),

    html.P('''
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam.
    ''', style={'color': 'darkred'})
])


@app.callback(
    Output(component_id='school-earnings', component_property='figure'),
    [
        Input(component_id='select-school', component_property='value'),
        Input(component_id='gap-range', component_property='value'),
    ]
)
def update_graph(selected_schools, gap_range):
    df = df_earning
    df = df[df.Gap.between(*gap_range)]
    if selected_schools:
        df = df[df.School.isin(selected_schools)]
    return {
        'data': [
            {'x': df.School, 'y': df.Gap, 'type': 'bar'}
        ]
    }


if __name__ == '__main__':
    app.run_server(debug=True)
