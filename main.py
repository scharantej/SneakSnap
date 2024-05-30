
from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # Fetch data on trending sneakers and their prices from an API
    response = requests.get('https://example.com/api/sneakers')
    sneakers = response.json()
    # Render the index page with the fetched data
    return render_template('index.html', sneakers=sneakers)

@app.route('/details/<int:sneaker_id>')
def details(sneaker_id):
    # Fetch the sneaker's data from an API
    response = requests.get('https://example.com/api/sneakers/{}'.format(sneaker_id))
    sneaker = response.json()
    return render_template('details.html', sneaker=sneaker)

if __name__ == '__main__':
    app.run()
