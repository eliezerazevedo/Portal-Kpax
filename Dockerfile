# Use uma imagem base oficial do Python
FROM python:3.12-slim

# Defina o diretório de trabalho
WORKDIR /app

# Copie o arquivo requirements.txt para dentro do container
COPY requirements.txt .

# Instale as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copie todo o código da aplicação para dentro do container
COPY . .

# Exponha a porta que a aplicação Flask vai rodar
EXPOSE 5555

# Comando para rodar a aplicação Flask
CMD ["python", "app.py"]