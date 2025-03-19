import dash
from dash import html

app = dash.Dash(__name__)

app.layout = html.Div([

    html.H1("Hello world!")

        ])

### Uruchomienie serwera
if __name__ == '__main__':
    app.run(port=8012, debug=True)