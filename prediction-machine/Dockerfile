FROM python:slim-buster
WORKDIR /prediction
RUN pip install --upgrade pip
RUN pip install flask
RUN pip install requests
RUN pip install scikit-learn
COPY . .
EXPOSE 5001
CMD ["python3","predict.py"]
