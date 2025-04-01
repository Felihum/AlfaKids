FROM python:latest

WORKDIR /app
ENV FLASK_APP app.py

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "-m", "flask", "db", "upgrade", "--host=0.0.0.0"]

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]