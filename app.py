from flask import *
import requests

app = Flask(__name__)

@app.route('/', methods=["GET"])
def get_chuck_norris_jokes():
    api_url = "https://api.chucknorris.io/jokes/random"
    data = requests.get(api_url).json()

    return "<img src='{}'></img></br> <strong>Endpoint data from Chuck Norris API: </strong></br>{}".format(
        data['icon_url'],data)


@app.route('/categories', methods=["GET"])
def get_chuck_norris_categories():
    list = requests.get("https://api.chucknorris.io/jokes/categories")
    return "{}".format(list.json())


if __name__ == '__main__':
    app.run(debug=True)
