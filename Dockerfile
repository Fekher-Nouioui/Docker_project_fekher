FROM python:3.8.5
MAINTAINER Fekher_Nouioui 
COPY . /app
WORKDIR /app/flask_app
RUN apt update && apt-get install -y libsndfile1
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["app.py"]
