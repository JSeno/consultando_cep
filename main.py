# Consumindo uma API utilizando o python
# Usando o viacep

# pip install requests

import requests


def main():
    

    print('####################')
    print('### Consulta CEP ###')
    print('####################')

    cep_input = input('Digite o CEP: ')

    if len(cep_input) != 8:
        print('CEP inválido')
        print('-----------------------------')
        exit()

    request = requests.get(f'https://viacep.com.br/ws/{cep_input}/json/')
    address_data = request.json()


    if 'erro' not in address_data:
        print('####################')
        print('####################')
        print('==> CEP ENCONTRADO <==')
        # print(request.json())
        print(f'CEP: {address_data["cep"]}')
        print(f'Logradouro: {address_data["logradouro"]}')
        print(f'Complemento: {address_data["complemento"]}')
        print(f'Bairro: {address_data["bairro"]}')
        print(f'Localidade: {address_data["localidade"]}')
        print(f'UF: {address_data["uf"]}')
        print(f'IBGE: {address_data["ibge"]}')
        print(f'Gia: {address_data["gia"]}')
        print(f'DDD: {address_data["ddd"]}')
        print(f'Siafi: {address_data["siafi"]}')

        print('####################')
        print('####################')

    else:
        print(f'CEP não encontrado você digitou: {cep_input}')
        exit()

    option = int(input('Deseja realizar uma nova consulta?\n1-SIM\n2-NÃO\n'))
    if option == 1:
        main()
    else:
        print('Saindo do programa')
        exit()

if __name__ == '__main__':
    main()
