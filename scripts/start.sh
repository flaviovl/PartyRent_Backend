#!/bin/bash
function_postgres_ready() {
python << END
import socket
import time
import os

port = int(os.environ["POSTGRES_PORT"])
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while True:
    try:
        s.connect(('pr-db', port))
        s.close()
        break
    except socket.error as ex:
        time.sleep(0.5)
END
}
echo "============> VERIFICAR PACOTES E INTALAR REQUERIMENTOS..."
pip freeze || pip install -r requirements.txt
echo "============> CRIAR NOVAS MIGRACOES - ALTERACAO MODELS..."
python3 manage.py makemigrations
echo "============> APLICAR MIGRAÇÕES..."
python3 manage.py migrate
echo "============> SERVIDOR RODANDO (0.0.0.0:8040)..."
exec python3 manage.py runserver 0.0.0.0:8040
