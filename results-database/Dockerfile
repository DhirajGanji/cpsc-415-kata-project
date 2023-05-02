FROM python:alpine3.17
WORKDIR /results
RUN pip install flask
RUN pip install requests
COPY . .
EXPOSE 5002
CMD ["python3","results.py"]
