import os
import json

from chalice import Chalice
from chalicelib import MESSAGE

app = Chalice(app_name='Multifile')

filename = os.path.join(
    os.path.dirname(__file__), 'chalicelib', 'app-config.json')
with open(filename) as f:
    config = json.load(f)


@app.route('/')
def index():
    if config['greet']:
        return {MESSAGE: 'world'}
    return {'bye': 'world'}
