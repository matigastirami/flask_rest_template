FROM python:3.10

RUN pip3 install pipenv

WORKDIR /app

COPY Pipfile Pipfile.lock ./

RUN pipenv install --system --deploy --ignore-pipfile

COPY . .

CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]