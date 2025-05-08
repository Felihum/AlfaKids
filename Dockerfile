FROM python:latest

WORKDIR /app
ENV FLASK_APP app.py

COPY . .

RUN pip3 install -r requirements.txt

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]