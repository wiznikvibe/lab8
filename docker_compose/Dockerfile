FROM python:3.7-alpine

WORKDIR /code

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["flask", "--app=app", "run", "--host=0.0.0.0"]
