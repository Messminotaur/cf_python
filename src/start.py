"""Cloud Foundry test"""
from flask import Flask
from flask import jsonify
import os
import requests

app = Flask(__name__)

port = int(os.getenv("PORT"))

@app.route('/')
def hello_world():
    return 'Hello World! I am running on port ' + str(port)
@app.route('/poe')
def poe_request():
    resp=requests.get('http://www.pathofexile.com/api/public-stash-tabs')
    if resp.status_code != 200:
        raise ApiError('Get http://www.pathofexile.com/api/public-stash-tabs failed: {}:'.format(resp.status_code))
    return jsonify([tab for tab in resp.json()['stashes'] if tab['public'] for item in tab['items'] if 'weapons' in item['category']  ])#if 'bows' in item['category']['weapons']])
        
# https://www.pathofexile.com/api/public-stash-tabs?id=220-1652-744-1341-230
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
