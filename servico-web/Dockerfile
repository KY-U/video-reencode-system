FROM python:3.12-slim

#definindo diretorio de trabalho
WORKDIR /app

#copiando arquivos de dependencias
COPY requirements.txt .

#instalando dependencias
RUN pip install --no-cache-dir -r requirements.txt

#copiando arquivos do projeto
COPY . .

#adicionando binarios do ffmpeg ao path do container
COPY ffmpeg_bin /app/bin

#adicionando binarios do ffmpeg ao path do container
ENV PATH="/app/bin:${PATH}"

#definindo variavel de ambiente da porta
ENV APP_PORT=5000

#expondo porta
EXPOSE 5000

#comando de inicializacao
CMD ["python", "app.py"]