import altair as alt
import pandas as pd
from dash import Dash, dcc, html, Input, Output

# Importing data from csv file
df = pd.read_csv("breed_traits.csv")

app = Dash(__name__)
def plot_altair(xcol):
    chart = alt.Chart(df, title = "How many Dogs?").mark_bar().encode(
        x=xcol,
        y='count()'
    ).interactive()
    return chart.to_html()

app = Dash(__name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
server = app.server

app.layout = html.Div([
        dcc.Dropdown(
            id='xcol', value='Energy Level',
            options=[{'label': i, 'value': i} for i in df.columns]),
        html.Iframe(
            id='scatter',
            style={'border-width': '0', 'width': '100%', 'height': '400px'},
            srcDoc=plot_altair(xcol='Energy Level'))])

@app.callback(
    Output('scatter', 'srcDoc'),
    Input('xcol', 'value'))
def update_output(xcol):
    return plot_altair(xcol)

if __name__ == '__main__':
    app.run_server(debug=True)