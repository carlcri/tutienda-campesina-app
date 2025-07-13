FROM alpine:latest

RUN apk add --update python3

RUN apk add py3-pip

WORKDIR /web-server

COPY ["./requirements.txt", "."]

RUN pip install -r requirements.txt --break-system-packages

COPY ["./main.py", "."]

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
