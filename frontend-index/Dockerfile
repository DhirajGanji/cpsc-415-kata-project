FROM python:alpine3.17
WORKDIR /frontend
RUN pip install flask
RUN pip install requests
COPY . .
EXPOSE 5000
CMD ["python3","home.py"]
