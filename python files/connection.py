from flask import Flask
from flask import render_template
import pymongo
import dash
from dash import dcc, html
import pandas as pd

app = Flask(__name__)
dash_app = dash.Dash(__name__, server=app, url_base_pathname='/dashboard/')

# MongoDB connection
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["India_Population"]
collection = db["data"]

# Fetch data from MongoDB and convert to DataFrame
data_from_mongodb = list(collection.find({}, {"_id": 0}))
df = pd.DataFrame(data_from_mongodb)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
# Dashboard layout

dash_app.layout = html.Div([
    html.H1(' Population Dashboard'),
    dcc.Graph(
        id='Population-graph',
        figure={
            'data': [
{'x': df['State'], 'y': df['Population'], 'type': 'bar', 'name': 'Population'},
{'x': df['State'], 'y': df['Male'], 'type': 'bar', 'name': 'Female Population'},
{'x': df['State'], 'y': df['Female'], 'type': 'bar', 'name': 'male Population'},
],
            'layout': {
'plot_bgcolor': colors['background'],
'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                },
                'title': 'Top 10 States wise Population'
            }
        }
    )
])

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
