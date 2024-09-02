FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

#adicionando binarios do ffmpeg ao path do container
COPY ffmpeg_bin /app/bin

ENV PATH="/app/bin:${PATH}"

ENV APP_PORT=5000

EXPOSE 5000

CMD ["python", "app.py"]