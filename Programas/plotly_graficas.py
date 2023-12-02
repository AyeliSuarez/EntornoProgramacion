import pandas
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, dash_table, callback, Input, Output
# dce -----> Dash Core Components
# html -----> Dash Intel Components

data = pd.read_csv("olimpiadas.csv", index_col=0)

def dashboard():
    data_pais=data.groupby("country", as_index=False).sum(numeric_only=True)
    g1 = px.line(data_pais, x="country", y=["gold", "silver", "bronze"])


    body = html.Div([
        html.H2("Datos Olimpiadas"),
        html.P("Objetivo DashBoard: Mostrar los resultados de las medallas de los paises"),
        html.Hr(),
        dash_table.DataTable(data=data.to_dict("records"), page_size=20),
        dcc.Dropdown(options=["all", "gold", "silver", "bronze"],
                     value="all", id="ddMedal"),
        dcc.Graph(figure=g1, id="figMedal")
    ])
    return body

@callback(
    Output(component_id="figMedal", component_property="Figure"),
    Input(component_id="ddMedal", component_property="Value")
)
def update_grafica(value_chosen):
    data_pais = data.groupby("country", as_index=False).sum(numeric_only=True)
    fig = px.line(data_pais, x="country", y=value_chosen)

if __name__ == "__main__":
    app = Dash(__name__)
    app.layout= dashboard()
    app.run(debug=True)


