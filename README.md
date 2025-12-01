# 📊 Sistema de Análise Econômica

O **Sistema de Análise Econômica** é uma plataforma desenvolvida em **Python + Django** para controle, análise e visualização de indicadores financeiros, permitindo gestão completa via interface web e integração com ferramentas externas como **Power BI**, através de uma API JSON.

O sistema permite cadastrar, editar, excluir e visualizar indicadores com cálculos automáticos de lucro e projeções.

---

## 🚀 Tecnologias Utilizadas

- **Python 3.11**
- **Django 5.2**
- **Django REST Framework**
- **HTML + Bootstrap**
- **SQLite (banco padrão do Django)**
- **Requests** (para consumo da API)
- **Power BI** (integração via API JSON)

---

## 📸 Interface do Sistema

### **Tela principal**
![Tela Home](docs/tela-home.png)

### **Dashboard de Indicadores**
![Dashboard](docs/dashboard.png)

---
## 📁 Estrutura do Projeto

Sistema-Analise-Economica/
│
├── economia/ # Configurações do projeto
├── indicadores/ # App principal (CRUD + API)
│ ├── models.py # Modelo Indicador
│ ├── views.py # Lógica das páginas e API
│ ├── urls.py # Rotas do app
│ ├── tests/ # Testes automatizados
│ └── templates/ # Interface HTML
│
├── usuarios/ # Sistema de login/autenticação
├── venv/ # Ambiente virtual
└── manage.py # Gerenciador Django

yaml
Copiar código

---

## ⚙️ Como Rodar o Projeto

### **1️⃣ Criar ambiente virtual**
python -m venv venv

2️⃣ Ativar ambiente
venv\Scripts\activate

3️⃣ Instalar dependências
pip install -r requirements.txt

4️⃣ Aplicar migrações
python manage.py migrate

5️⃣ Rodar servidor
python manage.py runserver

http://127.0.0.1:8000/

