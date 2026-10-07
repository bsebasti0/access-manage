a aliar já cria a extrutura do projecto e o ambiente virtual

instalação das dependencias adicionais

creação do banco de dados   ./app/api/core

creação dos models    ./app/models

atualizar banco de dados usando alembic
configurar o algo do banco de dados  ./alembic/env.py
comandos:
alembic init alembic
alembic revision --autogenerate -m "create controllers table"
alembic upgrade head

Criar as migrations


Criação  dos schemas   ./app/schemas
Criar todos os schemas servem para controlar os dados que venhem do front e os dados que na qual vai retornar para retornar exatamente o que nos queremos
teste: python -c "import app.schemas.user, app.schemas.controller, app.schemas.device, app.schemas.command, app.schemas.gateway; print('ok')"


