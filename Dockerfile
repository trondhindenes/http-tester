FROM python:3.9-slim-buster AS parent
WORKDIR /app
RUN pip install pipenv
COPY Pipfile /app/
COPY Pipfile.lock /app/
ENV PYTHONUNBUFFERED=1


FROM parent AS base
RUN pipenv install --deploy --system


FROM base as Prod
WORKDIR /app
COPY . .
ENTRYPOINT ["python", "doit.py"]
