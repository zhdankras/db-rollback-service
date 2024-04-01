FROM python:3.7.2-alpine
WORKDIR /db-rollback-service
COPY src requirements.txt ./
RUN pip3 install -r requirements.txt
CMD ["python3", "main.py"]
