FROM python:3.10

WORKDIR /opt/app
COPY internal/ internal/

COPY requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python", "-m", "internal"]