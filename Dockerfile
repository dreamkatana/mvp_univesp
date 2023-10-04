FROM python:3.10
EXPOSE 5002
WORKDIR /app
COPY ./requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .
#CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5001"]
#CMD ["gunicorn", "--bind", "0.0.0.0:80", "webapp:criar_app()"]
CMD ["flask", "--app", "webapp", "run", "--host", "0.0.0.0", "--port", "5002"]