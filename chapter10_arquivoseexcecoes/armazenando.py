import json
file_name = 'numbers.json'
"""numbers = [2, 3, 5, 7, 11, 13]

file_name = 'numbers.json'
with open(file_name, 'w') as file_object:
    json.dump(numbers, file_object)

with open(file_name) as file_object:
    numbers = json.load(file_object)
print(numbers)

filename = 'username.json'

def greet_user():
    try:
        with open(filename) as file_object:
            name = json.load(file_object)

    except FileNotFoundError:
        with open(filename, 'w') as file_object:
            name = input('Qual o seu nome?')
            json.dump(name, file_object)
            print(f'Bem vindo, {name}')

    else:
        print(f'Bem vindo de volta, {name}')


greet_user()




numero = 'favorito.json'

try:
    with open(numero) as file_object:
        favorito = json.load(file_object)
except FileNotFoundError:
    with open(numero, 'w') as file_object:
        favorito = int(input('Qual o seu número favorito?'))
        json.dump(favorito, file_object)
else:
    print(f'Já sei seu número favorito!! É o número {favorito}')"""




filename = 'username.json'



def new_user():
    with open(filename, 'w') as file_object:
        name = input('Então qual é o seu nome?')
        print(f'Seja bem vindo {name}')
        json.dump(name, file_object)


def greet_user():
    try:
        with open(filename) as file_object:
            name = json.load(file_object)

    except FileNotFoundError:
        with open(filename, 'w') as file_object:
            name = input('Qual o seu nome?')
            json.dump(name, file_object)
            print(f'Bem vindo, {name}')


    else:
        confirmacao = input(f'Seu nome é {name}? Responde com s ou n')

        if confirmacao == 's':
            print(f'Bem vindo de volta, {name}!')
        else:
            new_user()

greet_user()
















