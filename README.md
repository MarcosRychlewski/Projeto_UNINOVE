# API <img align="center" alt="Marcos-Python" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg">

[![NPM](https://img.shields.io/npm/l/react)](https://github.com/SquadUninove/API/blob/main/LICENSE) 

## Rota DE LOGIN/CREATE/LOGOUT de uma API!

## Sobre o Projeto

Back-end de um sistema, 
desenvolvido para a aula de Projetos do curso de ADS da Universidade Nove de Julho



## Tecnologias
- Python
- Django
- Django Rest Framework
- PostegreSQL
- Heroku




## Setup

- Criar diretório do projeto (mkdir nome_projeto)
- Criar venv (python -m venv venv)
- Add arquivos:

.gitignore

requirements.txt

- Install o Django
- Criar um projeto django (django-admin.py startproject setup .)
- Criar app das rotas (python manage.py startapp cardapio)
- Rodar o comando no terminal (python manage.py migrate) - criar as tabelas auth_user
- Cadastrar um super user (python manage.py createsuperuser)
- Install Rest Framework 
- Rodar o comando (python manage.py runserver)




# Documentação das Rotas

# Rotas-user
## POST LOGIN_USER
 https://api-squaduni.herokuapp.com/api/login/
 
    {
    "username": "admin",
    "password": "admin"
    }
    
## POST CREATE_USER
 https://api-squaduni.herokuapp.com/api/register/
 
    {
    "username": "admin",
    "password": "admin",
    "email":"marcoslindao@gmail.com"
    }
    
## POST LOGOUT_USER
 https://api-squaduni.herokuapp.com/api/logout/ 

