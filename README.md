# Gestor de Dívidas Pessoais

Aplicação desenvolvida para gerenciar despesas de uso comunitário. Qualquer pessoa pode utilizar esta aplicação e contribuir com seu desenvolvimento.

## 🛠️ Configuração das Variáveis de Ambiente

### 📝 Backend (.env)

Crie um arquivo `.env` na pasta `backend` com as seguintes variáveis:

```env
DB_USER=root                                   # Usuário do banco de dados
DB_PASSWORD=root                               # Senha do banco de dados
DB_HOST=localhost                              # Host do banco de dados
DB_PORT=3306                                   # Porta do banco de dados
DB_NAME=gestor_dividas                         # Nome do banco de dados
API_HOST=127.0.0.1                             # Host da API
API_PORT=8000                                  # Porta da API
API_RELOAD=True                                # Reload automático em desenvolvimento
CORS_ORIGINS=["http://localhost:5173"]         # Origens permitidas para CORS
API_TITLE="Gestor de Dívidas API"              # Título da API
API_DESCRIPTION="API para gerenciamento de dívidas pessoais"  # Descrição da API
API_VERSION="0.0.1"                           # Versão da API
JWT_SECRET_KEY="sua_chave_secreta_aqui"       # Chave secreta para JWT
JWT_ALGORITHM="HS256"                         # Algoritmo JWT
JWT_ACCESS_TOKEN_EXPIRE_MINUTES=30            # Tempo de expiração do token JWT
```


### 🎨 Frontend (.env)

Crie um arquivo `.env` na pasta `frontend` com as seguintes variáveis:

```env
PORT=5173    # Porta onde o frontend será executado
```


## 🚀 Passo a passo para executar o projeto

### ⚙️ Backend (FastAPI)

1. Entre na pasta backend:

```cd backend```


2. Atualize as dependências usando uv.py:

# Gera os arquivos de requirements
```
uv pip compile pyproject.toml -o requirements.txt
uv pip compile --extra dev pyproject.toml -o requirements-dev.txt
```

# Instala as dependências
``` uv pip sync requirements.txt requirements-dev.txt ```

# Atualiza todas as dependências
``` uv pip install -r pyproject.toml ```

3. Inicie o servidor:

``` python main.py ```


> O servidor backend estará rodando em `http://localhost:8000`

### 🌐 Frontend (Angular)

1. Entre na pasta frontend:

```cd frontend ```


2. Instale as dependências usando yarn:

``` yarn install ```


3. Inicie o servidor de desenvolvimento:

``` yarn dev ```


> O frontend estará disponível em `http://localhost:5173/` esta porta é definida apenas por ja estar no CORS uma vez que a porta padrão do Angular é 4200 e decidi usar a porta do VITE.
> 
> Nota: A porta padrão definida no .env é 5173, mas você pode configurar qualquer outra porta.
