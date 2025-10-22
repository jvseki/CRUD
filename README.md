# CRUD de Alunos e Cursos - Flask + SQLAlchemy + Bootstrap

## 📌 Descrição do Projeto

Este projeto é um **CRUD completo (Create, Read, Update, Delete)** desenvolvido em **Python com Flask e SQLAlchemy**, com interface profissional utilizando **Bootstrap 5**.  

O sistema permite gerenciar **Alunos** e **Cursos**, bem como realizar **matrículas de alunos em cursos**, criando um relacionamento **muitos-para-muitos**.  

O objetivo principal do projeto é servir como **exemplo prático de aplicação web**, demonstrando conceitos fundamentais de **bancos de dados relacionais, ORM, rotas Flask e interfaces responsivas**. É um projeto ideal para aprendizado ou portfólio.

---

## 🎯 Funcionalidades

### **Alunos**
- Listar todos os alunos cadastrados
- Adicionar novos alunos
- Editar informações de alunos existentes
- Excluir alunos
- Visualizar os cursos em que cada aluno está matriculado

### **Cursos**
- Listar todos os cursos cadastrados
- Adicionar novos cursos
- Editar informações de cursos existentes
- Excluir cursos
- Visualizar todos os alunos matriculados em cada curso

### **Matrículas**
- Matricular alunos em cursos
- Evitar duplicidade de matrículas
- Visualizar o relacionamento aluno ↔ curso de forma clara com **badges coloridos** na interface

---

## 💻 Tecnologias Utilizadas

- **Python 3.10+** – Linguagem de programação
- **Flask** – Framework web para Python
- **SQLAlchemy** – ORM para gerenciamento do banco de dados
- **SQLite** – Banco de dados leve para desenvolvimento local
- **Bootstrap 5** – Framework CSS para design responsivo e profissional
- **Jinja2** – Motor de templates do Flask para renderização dinâmica de páginas HTML

---

## 🛠 Estrutura do Projeto

```
CRUD/
│
├── app.py # Arquivo principal com rotas, modelos e lógica
├── templates/ # HTMLs do projeto
│ ├── index.html
│ ├── alunos.html
│ ├── adicionar_aluno.html
│ ├── editar_aluno.html
│ ├── cursos.html
│ ├── adicionar_curso.html
│ ├── editar_curso.html
│ └── matricular.html
└── static/ # Arquivos estáticos (CSS, JS, imagens) se necessário
```

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
- Python 3.10 ou superior instalado
- Pip (gerenciador de pacotes Python)

### Passos
1. **Clonar o repositório**
```bash
git clone <URL_DO_SEU_REPOSITORIO>
cd CRUD

Criar ambiente virtual (opcional, mas recomendado)

python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
pip install flask flask_sqlalchemy
Rodar o projeto

bash
Copiar código
python app.py
Acessar no navegador

cpp
Copiar código
http://127.0.0.1:5000

