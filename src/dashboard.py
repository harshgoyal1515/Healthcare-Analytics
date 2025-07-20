import pandas as pd
import dash
from dash import dcc, html, Input, Output
import plotly.express as px

# Load enhanced data
df = pd.read_csv("enhanced_healthcare.csv")

# Initialize the Dash app
app = dash.Dash(__name__)
app.title = "Healthcare Dashboard"

# Layout
app.layout = html.Div([
    html.H1("Healthcare Analytics Dashboard", style={"textAlign": "center"}),

    html.Label("Filter by Billing Category:"),
    dcc.Dropdown(
        id="billing-filter",
        options=[{"label": x, "value": x} for x in df["BillingCategory"].unique()],
        value="Medium"
    ),

    html.Br(),
    dcc.Graph(id="top-conditions"),

    html.Br(),
    dcc.Graph(id="billing-distribution"),

    html.Br(),
    dcc.Graph(id="stay-duration")
])

# Callbacks
@app.callback(
    [Output("top-conditions", "figure"),
     Output("billing-distribution", "figure"),
     Output("stay-duration", "figure")],
    [Input("billing-filter", "value")]
)
def update_dashboard(billing_category):
    filtered = df[df["BillingCategory"] == billing_category]

    fig1 = px.bar(
        filtered["Medical Condition"].value_counts().nlargest(10),
        title=f"Top 10 Conditions - {billing_category}",
        labels={"value": "Patient Count", "index": "Medical Condition"}
    )

    fig2 = px.histogram(
        filtered,
        x="Billing Amount",
        nbins=30,
        title=f"Billing Amount Distribution - {billing_category}"
    )

    fig3 = px.histogram(
        filtered,
        x="StayDuration",
        nbins=20,
        title=f"Stay Duration Distribution - {billing_category}"
    )

    return fig1, fig2, fig3

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
