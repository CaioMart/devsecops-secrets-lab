import os

DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
API_TOKEN = os.getenv("API_TOKEN")

print("Iniciando aplicação...")
print("Usuário do banco carregado:", DATABASE_USER)
print("Senha do banco carregada:", "***")
print("Token da API carregado:", "***")
