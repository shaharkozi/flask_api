FROM python:3.11.7-slim

COPY . /app

WORKDIR /app

ENV ENV=prod

RUN pip install --no-cache-dir -r requirements.txt

RUN python -m unittest tests/test_api.py

RUN rm player.csv

EXPOSE 80

CMD ["python", "./app.py"]


