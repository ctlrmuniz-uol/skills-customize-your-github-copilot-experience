# FastAPI REST API - Starter Code
# Tarefa: Construindo APIs REST com FastAPI

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

# Inicializar a aplicação FastAPI
app = FastAPI(
    title="Books API",
    description="Uma API simples para gerenciar uma coleção de livros",
    version="1.0.0"
)

# TODO: Definir os modelos Pydantic aqui
class Book(BaseModel):
    """Modelo completo de um livro com ID"""
    # TODO: Adicionar campos do livro aqui
    pass

class BookCreate(BaseModel):
    """Modelo para criar um novo livro (sem ID)"""
    # TODO: Adicionar campos do livro aqui (exceto id)
    pass

# Lista em memória para armazenar os livros (simula um banco de dados)
books_db: List[Book] = []

# Contador para IDs únicos
next_id = 1

# TODO: Implementar as rotas da API aqui

@app.get("/")
def read_root():
    """Rota de boas-vindas"""
    return {"message": "Bem-vindo à Books API!"}

# TODO: Implementar rota GET /books
@app.get("/books", response_model=List[Book])
def get_books():
    """Obter todos os livros"""
    pass

# TODO: Implementar rota POST /books
@app.post("/books", response_model=Book, status_code=201)
def create_book(book: BookCreate):
    """Criar um novo livro"""
    pass

# TODO: Implementar rota GET /books/{book_id}
@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    """Obter um livro específico por ID"""
    pass

# TODO: Implementar rota PUT /books/{book_id}
@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book: BookCreate):
    """Atualizar um livro existente"""
    pass

# TODO: Implementar rota DELETE /books/{book_id}
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    """Remover um livro"""
    pass

# Função para adicionar dados de exemplo
def add_sample_books():
    """Adiciona alguns livros de exemplo ao iniciar a aplicação"""
    # TODO: Adicionar livros de exemplo aqui
    pass

# Adicionar dados de exemplo ao iniciar
# TODO: Descomente a linha abaixo após implementar add_sample_books()
# add_sample_books()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)