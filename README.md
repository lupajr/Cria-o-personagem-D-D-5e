# 🛡️ D&D 5e Random Character Generator

Um gerador de personagens para Dungeons & Dragons 5ª Edição construído com **FastAPI** e **Vanilla JavaScript**. O sistema cria personagens com atributos otimizados por classe, aplica bônus raciais e permite salvar/excluir o histórico em um banco de dados flat-file (.txt).

## 🚀 Funcionalidades

- **Geração Inteligente:** Atributos gerados via 4d6 (drop lowest) e distribuídos conforme a prioridade da classe (ex: Inteligência para Magos).
- **Bônus Raciais:** Aplicação automática de modificadores de raça (Humano, Elfo, Anão, Meio-Orc).
- **Persistência em TXT:** Salva os personagens criados em um arquivo de texto para consulta posterior.
- **Interface Web:** Frontend responsivo integrado para gerar, visualizar e deletar heróis.
- **API REST:** Endpoints organizados para integração com outros sistemas.

## 🛠️ Tecnologias Utilizadas

* **Backend:** [FastAPI](https://fastapi.tiangolo.com/) (Python 3.9+)
* **Servidor ASGI:** [Uvicorn](https://www.uvicorn.org/)
* **Frontend:** HTML5, CSS3 e JavaScript (Fetch API)
* **Persistência:** JSON em arquivo de texto (.txt)

## 📂 Estrutura do Projeto

```text
├── main.py              # Rotas da API e configuração do servidor
├── logic.py             # Regras de D&D e lógica de sorteio
├── requirements.txt     # Dependências do projeto
├── personagens_salvos.txt # "Banco de dados" (gerado automaticamente)
└── static/
    └── index.html       # Interface do usuário
💻 Como Rodar Localmente
Clone o repositório:

Bash

git clone [https://github.com/seu-usuario/nome-do-repo.git](https://github.com/seu-usuario/nome-do-repo.git)
cd nome-do-repo
Instale as dependências:


pip install -r requirements.txt
Inicie o servidor:


uvicorn main:app --reload
Acesse no navegador: http://127.0.0.1:8000

🌐 Deploy no Render
Para hospedar este projeto no Render:

Conecte seu repositório do GitHub ao Render.

Selecione Web Service.

Use as configurações:

Runtime: Python 3

Build Command: pip install -r requirements.txt

Start Command: uvicorn main:app --host 0.0.0.0 --port $PORT

📖 Endpoints da API
GET /: Retorna a interface web.

GET /personagem: Gera um novo personagem e salva no histórico.

GET /historico: Lista todos os personagens salvos.

DELETE /personagem/{id}: Remove um personagem específico pelo ID.

Criado por Luiz Paulo - 2026
