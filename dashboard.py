import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Sample data
df = pd.DataFrame({
    "Match": [1,2,3,4,5,6],
    "Runs": [45,78,102,56,89,120],
    "StrikeRate": [110,125,140,115,130,150]
})

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Cricket Performance Dashboard"),

    dcc.Dropdown(
        id="metric",
        options=[
            {"label": "Runs", "value": "Runs"},
            {"label": "Strike Rate", "value": "StrikeRate"}
        ],
        value="Runs"
    ),

    dcc.Graph(id="graph")
])

@app.callback(
    dash.Output("graph", "figure"),
    dash.Input("metric", "value")
)
def update_chart(metric):
    fig = px.line(df, x="Match", y=metric, markers=True)
    return fig

if __name__ == "__main__":
    app.run(debug=True)