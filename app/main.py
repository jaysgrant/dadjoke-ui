#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module queries the specified URL endpoint to retrieve the json data for a joke
and returns it to the end user in a web viewable format.
"""

import os
import json
import requests
from flask import Flask, send_from_directory, render_template


def get_data():
    """
    This function queries the specified URL to retrieve the json out put.
    """
    try:
        data_url = os.environ['DATA_URL']
        r = requests.get(data_url)
        json_data = json.loads(r.text)
        return json_data
    except ValueError:
        print('Decoding JSON has failed')


def joke_builder():
    """
    This function builds the opener and punchline portions that will be displayed to the end user.
    """
    try: 
        json_data = get_data()
        joke = (json_data["Joke"])
        joke_opener = (joke["Opener"])
        joke_punchline = (joke["Punchline"])
        return joke_opener, joke_punchline
    except ValueError:
        print('Decoding JSON has failed')
    except requests.exceptions.TooManyRedirects:
        print(["Too many redirects."])
    except requests.exceptions.RequestException as requests_e:
        print(requests_e)


app = Flask(__name__)
@app.route("/")
def joke():
    """
    This function renders the index.html page that is returned to the end user.
    """
    joke_opener, joke_punchline = joke_builder()
    return render_template('index.html', joke=joke_opener, punchline=joke_punchline)


@app.route('/favicon.ico')
def favicon():
    """
    This function renders the the favicon.ico file.
    """
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/healthz', methods=['GET'])
def get_healthz():
    """
    This function renders the health check endpoint.
    """
    return "OK"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
