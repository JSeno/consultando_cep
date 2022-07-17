Busca de cep utilizando o viacep.com.br com python

[]: # Language: markdown
[]: # Path: readme.md

Antes de começar precisa instalar a biblioteca requests

    `pip install requests`

Após instalar será necessário fazer o import da biblioteca requests

    `import requests`

Após importar podemos fazer a requisição do cep

    `response = requests.get('https://viacep.com.br/ws/{CEP BUSCADO}}/json/')`

As respostas serão armazenadas na variável response e seu retorno será em formato json:
    
    `response.json()`

