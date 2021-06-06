import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np

data = pd.read_csv("avocado.csv")
data = data.query("type == 'conventional' and region == 'Albany'")
data["Date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")
data.sort_values("Date", inplace=True)

external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?family=Roboto:wght@500&display=swap",
        "rel": "stylesheet",
    },
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Analise Sensor data"

graph1 = html.Div(
    dcc.Graph(
        config={"displayModeBar": False},
        figure={
            "data": [
                {
                    "x": data["Date"],
                    "y": data["AveragePrice"],
                    "type":"lines",
                    "hovertemplate": "$%{y:.2f}"
                    "<extra></extra>"
                },
            ],
            "layout": {
                "title": {
                    "text": "Average Signal",
                    "x": 0.05,
                    "xanchor": "left",
                },
                "xaxis": {"fixedrange": True},
                "yaxis": {
                    "tickprefix": "%",
                    "fixedrange": True,
                },
                "colorway": ["#17B897"],
            },
        },
    ),
    className="card graph-col1",
)

graph2 = html.Div(
    children=[
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["Date"],
                        "y": data["Total Volume"],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "Total Signal"},
            },
        ),
    ],
    className="card graph-col2",
)

graphContainer = html.Div(
    children=[
        html.Div(
            children=[
                graph1,
                graph2,
            ],
            className="graph-row",
        )
    ],
    className="container",
)

app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.H1(
                    children="Sensor Analytics",
                    className="header-title"
                ),
                html.P(
                    children="Analye the behavior of sensor data from mcu"
                ),
            ],
            className="header",
        ),

        graphContainer,
        graphContainer,
    ],
)

if __name__ == "__main__":
    app.run_server(debug=True)
