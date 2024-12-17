# Use a imagem base oficial do Python
FROM python:3.13.1-slim

# Minimize mensagens e garanta consistência nas instalações
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Defina o diretório de trabalho
WORKDIR /app

# Instale as dependências do sistema operacional necessárias para Python
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copie e instale dependências antes do código para aproveitar o cache
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copie o código da aplicação para dentro do container
COPY . .

# Exponha a porta que a aplicação Flask vai rodar
EXPOSE 5555

# Defina o comando para rodar a aplicação
CMD ["python", "app.py"]
