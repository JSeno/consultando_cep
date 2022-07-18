# Consumindo uma API utilizando o python
# Usando o viacep

# pip install requests

import re

import requests


def main():
    

    print('####################')
    print('### Consulta CEP ###')
    print('####################')

    cep_input = input('Digite o CEP: ')
    cep_clean = re.sub('[^0-9]', '', str(cep_input))
    print(f'O cep digitado foi: {cep_clean}')

    if len(cep_clean) != 8:
        print('CEP inválido')
        print('-----------------------------')
        exit()

    request = requests.get(f'https://viacep.com.br/ws/{cep_clean}/json/')
    address_data = request.json()


    if 'erro' not in address_data:
        print('####################')
        print('####################')
        print('==> CEP ENCONTRADO <==')
        # print(request.json())
        print(f'CEP: {address_data.get("cep", None)}')
        print(f'Logradouro: {address_data.get("logradouro", None)}')
        print(f'Complemento: {address_data.get("complemento", None)}')
        print(f'Bairro: {address_data.get("bairro", None)}')
        print(f'Localidade: {address_data.get("localidade", None)}')
        print(f'UF: {address_data.get("uf", None)}')
        print(f'IBGE: {address_data.get("ibge", None)}')
        print(f'Gia: {address_data.get("gia", None)}')
        print(f'DDD: {address_data.get("ddd", None)}')
        print(f'Siafi: {address_data.get("siafi", None)}')

        print('####################')
        print('####################')

    else:
        print(f'CEP não encontrado você digitou: {cep_clean}')
        exit()

    option = int(input('Deseja realizar uma nova consulta?\n1-SIM\n2-NÃO\n'))
    if option == 1:
        main()
    else:
        print('Saindo do programa')
        exit()

if __name__ == '__main__':
    main()
