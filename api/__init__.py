from flask import Flask
from api.config.cache import BaseConfig
from flask_caching import Cache
from api.config.debugger import initialize_flask_server_debugger_if_needed

initialize_flask_server_debugger_if_needed()

app = Flask(__name__)

app.config.from_object(BaseConfig)
cache = Cache(app)

from api.routes import item

app.run(debug=True)