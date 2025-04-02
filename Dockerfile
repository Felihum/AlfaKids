FROM python:latest

WORKDIR /app
ENV FLASK_APP app.py

#COPY requirements.txt requirements.txt
COPY . .

RUN pip3 install -r requirements.txt
#RUN flask db upgrade

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]