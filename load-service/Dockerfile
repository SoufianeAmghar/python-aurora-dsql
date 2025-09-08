FROM python:3.9-slim

WORKDIR /app

COPY pyproject.toml poetry.lock /app/
RUN pip install poetry && poetry config virtualenvs.create false && poetry install --no-root

RUN apt-get update && apt-get install -y curl unzip \
    && curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
    && unzip awscliv2.zip && ./aws/install \
    && rm -rf awscliv2.zip aws


COPY . /app

CMD ["poetry", "run", "python", "load.py"]
