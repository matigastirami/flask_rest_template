from functools import cache
from flask import Flask
from api.config.cache import BaseConfig
from flask_caching import Cache

app = Flask(__name__)

app.config.from_object(BaseConfig)
cache = Cache(app)

from api.routes import item

app.run(debug=True)