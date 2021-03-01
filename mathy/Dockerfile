FROM python:latest
COPY ../mathy .
RUN pip3 install -r requirements.txt
EXPOSE 5001
ENTRYPOINT ["gunicorn"  , "-b", "0.0.0.0:5001", "app:app"]