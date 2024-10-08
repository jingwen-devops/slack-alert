FROM python:3.12-alpine3.20
WORKDIR /workspace
COPY . .
RUN pip3 install -r /workspace/requirements.txt
CMD ["python3", "/workspace/app.py"]
