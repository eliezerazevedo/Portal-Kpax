from flask import Flask, render_template, request, redirect
import requests
import os
import json
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

app = Flask(__name__)

# URL e tokens de autenticação
url = os.getenv('API_URL')
access_token = os.getenv('ACCESS_TOKEN')
csrf_token = os.getenv('CSRF_TOKEN')

# Carregar os usuários do arquivo .env e parsear a string JSON
users = json.loads(os.getenv('USERS', '{}'))

@app.route('/')
def index():
    return render_template('index.html', users=users)

@app.route('/sharepoint')
def sharepoint():
    sharepoint_url = os.getenv('SHAREPOINT')
    if sharepoint_url:
        return redirect(sharepoint_url)  # Redireciona para o link do SharePoint
    else:
        return "Erro: URL do SharePoint não encontrada."

@app.route('/download', methods=['GET'])
def download():
    name = request.args.get('name')
    if name:
        data = {
            'parent_type': 'account',
            'parent_id': '526',
            'name': f'Novo agente ({name})'
        }

        headers = {
            'accept': 'application/json',
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json',
            'X-CSRF-TOKEN': csrf_token
        }

        # Enviando a requisição POST
        response = requests.post(url, json=data, headers=headers)

        if response.status_code == 201:  # Código de sucesso para criação
            response_data = response.json()
            agent_installer_url = response_data.get('agent_installer_binary_url')

            if agent_installer_url:
                return redirect(agent_installer_url)
            else:
                return "Erro: URL do instalador não encontrada."
        else:
            return f"Erro: {response.status_code}"

    return 'Nome não fornecido.'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5555)
