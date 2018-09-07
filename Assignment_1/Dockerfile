FROM python:2.7.15-alpine
MAINTAINER Prasanna Ranganathan "prassanna.mit@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app/app.py"]
