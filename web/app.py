from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def index():
    resp = requests.get(
        url = 'http://127.0.0.1:9080/crawl.json?start_requests=True&spider_name=imdb2019'
    ).json()

    items = resp.get('items')

    return render_template('index.html', movies=items)


if __name__ == '__main__':
    app.run(debug=True)
