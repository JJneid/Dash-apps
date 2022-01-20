import dash
import dash_core_components as dcc
import dash_html_components as html
import os

app = dash.Dash(__name__)
server = app.server

app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

app.layout = html.Div([
    html.H2('Who are you??'),
    html.Div([    dcc.Dropdown(
            id='dropdown_name',
            options=[{'label': i, 'value': i} for i in ['Elsa', 'Ralph', 'Maria',"Bruno"]],
            value='Maria'
        )]),
    html.H2(id='display-name-value'),
    html.H2('Choose next carefully!!'),
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': i, 'value': i} for i in ['LA', 'NYC', 'MTL']],
        value='LA'
    ),
    html.H2(id='display-value')
])


@app.callback(dash.dependencies.Output('display-name-value', 'children'),
              [dash.dependencies.Input('dropdown_name', 'value')])
def display_value(value):
    return 'Hello "{}"'.format(value)

@app.callback(dash.dependencies.Output('display-value', 'children'),
              [dash.dependencies.Input('dropdown', 'value')])
def display_value(value):
    return 'Your next destination will be "{}"'.format(value)

if __name__ == '__main__':
    app.run_server(debug=True)
