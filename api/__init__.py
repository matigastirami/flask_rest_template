from flask import Flask

app = Flask(__name__)

from api.routes import item

app.run(debug=True)