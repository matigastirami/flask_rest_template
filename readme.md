# Description
* Single Flask REST API template to start developing quickly and avoid wasting time in configuring a project from zero.
* Supports both local and docker environment (I highly encourage you to use docker-compose)

# What it includes
* Example API route
* Basic example test
* PostgreSQL configuration via SQLAlchemy
* Extended SQLAlchemy Base class with model serializer
* MongoDB configuration (Pending)
* RabbitMQ connection and configuration (Pending)
* Redis caching
* Docker support
* Hotreload for file changes (Via Flask debug option, only available when `FLASK_ENV=development`)

# What it does not includes
* Error handling
* Logging

# Running the api locally
1. `pipenv install` to install a venv and all the dependencies
2. `pipenv shell` to activate the venv
3. Set the FLASK_APP env variable: `export FLASK_APP=api` or `$env:FLASK_APP='api'` (Powershell)
4 `pipenv run flask run --port=80` to run the app

# Running docker-compose
1. Open the terminal and execute `docker-compose up --build pythonapp`

# Calling the API
1. Open your favorite REST client
2. GET http://localhost:80?name=yourname

# Technologies on this template
* Python
* Flask
* SQLAlchemy
* PostgreSQL
* SQLite
* RabbitMQ
* MongoDB
* Redis

# Pending
* Enable a command to allow the user that desires to use this template, to create a project with the desired dependencies, this way avoiding the necessity to delete each of the unused packages. For example:
`flask-api create-project --sql=true --mongodb=false --rabbitmq=false`
* Enable a command to add missing packages maybe?
`flask-api enable-packages --sql`
* Add logging
* Add error handling