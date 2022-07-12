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

# Running docker-compose (Normal Mode)
* Open the terminal and execute `docker-compose up --build pythonapp`

# Running docker-compose (Debug Mode for VS Code)
1. Add `- DEBUGGER=True` to docker-compose.yml in the `pythonapp_dev` environment 
2. Open the terminal and execute `docker-compose up --build pythonapp`
3. Press F5 when the terminal ask you for.
4. Start adding breakpoints!

# Calling the API
1. Open your favorite REST client
2. Start executing your requests. CURL examples:

## Create an item
```bash
curl --location --request POST 'localhost:80/items' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "test",
    "description": "test"
}'
```

## Get all items
```bash
curl --location --request GET 'localhost:80/items'
```

# Technologies on this template
* [Python](https://docs.python.org/3/)
* [Flask](https://flask.palletsprojects.com/en/2.1.x/)
* [SQLAlchemy](https://www.sqlalchemy.org/)
* [PostgreSQL](https://www.postgresql.org/)
* [SQLite](https://www.sqlite.org/index.html)
* [RabbitMQ](https://www.rabbitmq.com/)
* [MongoDB](https://www.mongodb.com/)
* [Redis](https://redis.io/)

# Pending
* Enable a command to allow the user that desires to use this template, to create a project with the desired dependencies, this way avoiding the necessity to delete each of the unused packages. For example:
`flask-api create-project --sql=true --mongodb=false --rabbitmq=false`
* Enable a command to add missing packages maybe?
`flask-api enable-packages --sql`
* Add logging
* Add error handling
* Add debug mode instructions for non-docker env

# VS Code troubleshooting
* If dependencies show a message that couldn't be found, do:
1. (CTRL/CMD) + SHIFT + P
2. Look for `Python: Select interpreter` option
3. On the dropdown select the venv related to the pipenv instance you are working