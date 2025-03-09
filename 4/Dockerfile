FROM e3tow1c/care-base:v1 

WORKDIR /app-hello

RUN apk add --no-cache python3
RUN echo 'print("Hello, World!")' > /hello.py

CMD ["python3", "/hello.py"]