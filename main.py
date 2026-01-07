from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import json
import os

# Importa a lógica que criamos no outro arquivo
from logic import generate_character

app = FastAPI()

# 1. Configuração ÚNICA de CORS (incluindo DELETE)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

DB_FILE = "personagens_salvos.txt"

# 2. Rota Principal: Entrega o index.html
@app.get("/")
async def read_index():
    # Verifica se o arquivo existe antes de tentar entregar
    path = os.path.join("static", "index.html")
    if os.path.exists(path):
        return FileResponse(path)
    return {"error": "Pasta 'static' ou arquivo 'index.html' nao encontrado."}

# 3. API: Gerar Personagem
@app.get("/personagem")
def get_character():
    personagem = generate_character()
    
    # Salva no arquivo TXT
    with open(DB_FILE, "a", encoding="utf-8") as f:
        linha = json.dumps(personagem, ensure_ascii=False)
        f.write(linha + "\n")
        
    return personagem

# 4. API: Listar Histórico
@app.get("/historico")
def get_historico():
    personagens = []
    if not os.path.exists(DB_FILE):
        return []
    
    with open(DB_FILE, "r", encoding="utf-8") as f:
        for linha in f:
            if linha.strip():
                personagens.append(json.loads(linha))
    return personagens

# 5. API: Deletar Personagem
@app.delete("/personagem/{char_id}")
def delete_character(char_id: str):
    if not os.path.exists(DB_FILE):
        raise HTTPException(status_code=404, detail="Arquivo não encontrado")

    personagens_restantes = []
    encontrado = False
    
    with open(DB_FILE, "r", encoding="utf-8") as f:
        for linha in f:
            if not linha.strip(): continue
            p = json.loads(linha)
            if p.get("id") == char_id:
                encontrado = True
            else:
                personagens_restantes.append(p)
    
    if not encontrado:
        raise HTTPException(status_code=404, detail="ID não encontrado")

    with open(DB_FILE, "w", encoding="utf-8") as f:
        for p in personagens_restantes:
            f.write(json.dumps(p, ensure_ascii=False) + "\n")
                
    return {"status": "sucesso"}

# 6. Monta a pasta static (OPCIONAL: para carregar CSS ou Imagens extras)
if os.path.exists("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")
    
