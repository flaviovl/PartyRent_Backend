#!/bin/bash

function_postgres_ready() {
python << END
import socket
import time
import os

port = int(os.environ["POSTGRES_PORT"])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('pr-db', port))
s.close()
END
}

echo "============> VERIFICAR PACOTES E INTALAR REQUERIMENTOS..."
pip freeze || pip install -r requirements.txt

# echo "==> COPIAR VARIAVEIS DE DESENVOLVIMENTO..."
# cp contrib/env-sample .env

until function_postgres_ready; do
    >&2 echo "============> POSTGRES INDISPINIVEL, AGUARDANDO BD..."
    sleep 1
done
echo "============> POSTGRES CONECTADO"

echo "============> CRIAR NOVAS MIGRACOES - ALTERACAO MODELS..."
python3 manage.py makemigrations

echo "============> APLICAR MIGRAÇÕES..."
python3 manage.py migrate

echo "============> SERVIDOR RODANDO (0.0.0.0:8040)..."
exec python3 manage.py runserver 0.0.0.0:8040
