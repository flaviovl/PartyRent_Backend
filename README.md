# G7 - PartyRent Backend
## Visão geral

A PartyRent é uma pequena empresa voltada a realização de aluguel para artigos diversos para festas. Mesas, cadeiras, móveis diversos e outros itens para a realização de aniversário, casamento, formaturas e demais eventos. A ideia do Projeto e realizar uma melhora no processo da empresa, realizando o desenvolvimento de uma ferramenta web para facilitar o processo de aluguel dos itens.

## Guia de Instalação

Essa aplicação tem seu ambiente configurado através de conteiners [Docker](https://www.docker.com), portanto, tem como pré-requisitos a instalação do [Docker](https://www.docker.com/get-started) e [Docker-compose](https://docs.docker.com/compose/install/).

Também é necessário ter o [Git](https://git-scm.com) instalado para clonar o repositório.

### **Back-end**:

Clonar o repositório:
  
``` bash
git clone git@github.com:UnBArqDsw2021-2/2021.2_G7_PartyRent_Backend.git
```
    

### Instalação Local (linux)

``` bash
cd 2021.2_G7_PartyRent_Backend
```
``` bash
python3 -m venv .venv
```
``` bash
source .venv/bin/activate
```
``` bash
pip install -r requirements.txt
```
``` bash
cp contrib/.env-sample-local .env
```
``` bash
python manage.py makemigrations
```
``` bash
python manage.py migrate
```
``` bash
python manage.py runserver  
```  

Agora abra o navegador e vá para: "http://localhost:8000" e você deve ver a tela inicial do Django:  

### Instalação Local (windows)

``` bash
cd 2021.2_G7_PartyRent_Backend
```
``` bash
python -m venv venv   
```
``` bash
.\venv\Scripts\Activate.ps1 
```
``` bash
pip install -r requirements.txt
```
``` bash
cp contrib/.env-sample-local .env
```
``` bash
python manage.py makemigrations
python3 -m venv .venv
```
``` bash
source .venv/bin/activate
```
``` bash
pip install -r requirements.txt
```
``` bash
cp contrib/.env-sample-local .env
```
``` bash
python manage.py migrate
```
``` bash
python manage.py runserver  
```  

Agora abra o navegador e vá para: "http://localhost:8000" e você deve ver a tela inicial do Django:  
    
    
### Usando Docker  
    
Copiar arquivo de variaveis de ambiente de desenvolvimento:  
``` bash
cp contrib/.env-sample-docker .env
```
    
Execução do conteiner:
``` bash
sudo docker-compose up
```

Agora abra o navegador e vá para: "http://0.0.0.0:8000" e você deve ver a tela inicial do Djang  
    

### **Front-end:**

Para instalar a camada front-end da aplicação basta seguir os passos de instalação descritos [aqui](https://github.com/UnBArqDsw2021-2/2021.2_G7_PartyRent_Frontend)

