import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

class DashboardApp:
    def __init__(self, df):
        self.df = df
        self.app = dash.Dash(__name__)

    def layout(self):
        fig = px.scatter(self.df, x='quantity', y='price',
                         color='is_fraud', size='total_value',
                         hover_data=['transaction_id', 'supplier_id', 'product_id'])
        self.app.layout = html.Div([
            html.H1("SmartSupplyGuard Dashboard"),
            dcc.Graph(figure=fig)
        ])

    def run(self):
        self.layout()
        self.app.run_server(debug=True)
