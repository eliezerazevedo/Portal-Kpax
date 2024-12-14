
# Portal-Kpax

Portal para gerar agentes no sistema Kpax ACD-INC.

## Instruções para Execução via Docker

Este repositório contém uma aplicação Flask que se conecta ao sistema Kpax ACD-INC para gerar agentes. A aplicação é configurada através de variáveis de ambiente, que devem ser definidas em um arquivo `.env`.

### Passos para Execução

### 1. Renomear o Arquivo de Exemplo

Renomeie o arquivo `exemplo.env` para `.env`:

```bash
mv exemplo.env .env
```

### 2. Editar o Arquivo `.env`

Abra o arquivo `.env` e edite as credenciais com as informações geradas no portal de API do Kpax.

Aqui está um exemplo de como o arquivo `.env` deve ser estruturado:

```ini
API_URL='https://ksc.kpax.cloud/api/v1/agents'
ACCESS_TOKEN=seu_token_de_acesso
CSRF_TOKEN=seu_token_CSRF
SHAREPOINT='url_do_sharepoint'
USERS='{
    "Eliezer Azevedo": "Novo agente (Eliezer Azevedo)",
    "Evandro Santos": "Novo agente (Evandro Santos)",
    "Geovanio Rodrigues": "Novo agente (Geovanio Rodrigues)",
    "Hygor Fernando": "Novo agente (Hygor Fernando)",
    "Julio Cesar": "Novo agente (Julio Cesar)",
    "Leandro Milhomens": "Novo agente (Leandro Milhomens)",
    "Lucas Ramos": "Novo agente (Lucas Ramos)",
    "Renato Oliveira": "Novo agente (Renato Oliveira)"
}'
```

Substitua os valores de `ACCESS_TOKEN`, `CSRF_TOKEN` pelos valores corretos gerados no portal de API do Kpax.

### 3. Construir e Subir o Contêiner Docker

Execute os seguintes comandos para construir e rodar o contêiner Docker:

**Construir a imagem Docker:**

```bash
docker-compose build
```

**Rodar o contêiner Docker em segundo plano:**

```bash
docker-compose up -d
```

### 4. Acessar a Aplicação

Após rodar o contêiner, a aplicação estará disponível no navegador em:

```
http://localhost:5555
```

### 5. Parar o Contêiner

Caso precise parar o contêiner, use o seguinte comando:

```bash
docker-compose down
```

Isso encerrará o contêiner.
