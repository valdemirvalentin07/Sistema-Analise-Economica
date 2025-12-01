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




## 📸 Interface do Sistema

### **Tela login**

<img width="1863" height="881" alt="Captura de tela 2025-12-01 125651" src="https://github.com/user-attachments/assets/f8c23b00-71cd-44c9-98ab-bda2c945004b" />


### **Tela principal**

---<img width="1854" height="900" alt="Captura de tela 2025-12-01 130256" src="https://github.com/user-attachments/assets/2eb1b7ad-bb50-4d0e-a089-4cfc9b9f39b5" />



### **Lista de Indicadores**


<img width="1541" height="690" alt="Captura de tela 2025-12-01 124810" src="https://github.com/user-attachments/assets/a6363361-fc0d-442f-bfbd-4e0d4af1a82a" />


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


### **Cobertura de testes**

<img width="1329" height="665" alt="image" src="https://github.com/user-attachments/assets/e12ead62-d293-4fbc-afb2-0a4620faac93" />




## ⚙️ Como Rodar o Projeto

### **1️⃣ Criar ambiente virtual**
python -m venv venv

### **2️⃣ Ativar ambiente**

venv\Scripts\activate

### **3️⃣ Instalar dependências**

pip install -r requirements.txt

### **4️⃣ Aplicar migrações**

python manage.py migrate

### **5️⃣ Rodar servidor**

python manage.py runserver

http://127.0.0.1:8000/

