import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

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


if __name__ == '__main__':
    app.run_server(debug=True)
