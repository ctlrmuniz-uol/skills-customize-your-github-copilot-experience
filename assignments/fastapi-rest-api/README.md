# 📘 Assignment: Construindo APIs REST com FastAPI

## 🎯 Objective

Nesta tarefa, você aprenderá a construir uma API REST completa usando o framework FastAPI do Python. Você criará uma API para gerenciar uma lista de livros, implementando operações CRUD (Create, Read, Update, Delete) e validação de dados com modelos Pydantic.

## 📝 Tasks

### 🛠️ Configurar o Ambiente FastAPI

#### Description
Configure um projeto FastAPI básico e crie sua primeira rota. Você instalará as dependências necessárias e criará a estrutura inicial da API.

#### Requirements
Completed program should:

- Instalar FastAPI e Uvicorn usando pip
- Criar um arquivo `main.py` com uma aplicação FastAPI básica
- Implementar uma rota GET de boas-vindas em "/"
- Executar o servidor de desenvolvimento e testar no navegador


### 🛠️ Criar Modelo de Dados com Pydantic

#### Description
Defina modelos de dados usando Pydantic para representar livros em sua API. Isso garantirá validação automática de dados e documentação clara da API.

#### Requirements
Completed program should:

- Criar uma classe `Book` com campos: id, title, author, publication_year, genre
- Usar tipos de dados apropriados (int, str) e validações
- Criar um modelo `BookCreate` para criação de novos livros (sem id)
- Implementar validação de ano de publicação (deve ser positivo e não futuro)


### 🛠️ Implementar Operações CRUD

#### Description
Implemente todas as operações CRUD para gerenciar livros na API. Use uma lista em memória para armazenar os dados (sem banco de dados por enquanto).

#### Requirements
Completed program should:

- POST /books - Criar um novo livro
- GET /books - Listar todos os livros
- GET /books/{book_id} - Obter um livro específico por ID
- PUT /books/{book_id} - Atualizar um livro existente
- DELETE /books/{book_id} - Remover um livro
- Retornar códigos de status HTTP apropriados (200, 201, 404)


### 🛠️ Adicionar Documentação e Validação

#### Description
Melhore sua API com documentação automática, tratamento de erros e validação adicional de dados.

#### Requirements
Completed program should:

- Adicionar descriptions e tags para todas as rotas
- Implementar tratamento de erro 404 para livros não encontrados
- Adicionar validação para IDs de livros (devem ser positivos)
- Testar a documentação automática em /docs
- Adicionar pelo menos 3 livros de exemplo ao iniciar a API