# this is alpine linux image
FROM e3tow1c/care-hello:latest

# in stalling pip3 for python3 in alpine linux
RUN apk add --no-cache py3-pip python3-dev mysql-dev pkgconfig gcc musl-dev

WORKDIR /app

COPY . .

# Create and use virtual environment for pip installations
RUN python3 -m venv /app/venv
ENV PATH="/app/venv/bin:$PATH"

RUN pip install -r requirements.txt

CMD ["python3", "app.py"]