a aliar já cria a extrutura do projecto e o ambiente virtual

instalação das dependencias adicionais

creação do banco de dados   ./app/api/core

creação dos models    ./app/models
Criação  dos schemas   ./app/schemas

atualizar banco de dados usando alembic
configurar o algo do banco de dados  ./alembic/env.py
comandos:
alembic init alembic
alembic revision --autogenerate -m "create controllers table"
alembic upgrade head

Criar as migrations
