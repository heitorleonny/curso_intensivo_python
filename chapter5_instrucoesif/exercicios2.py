usuarios = []

if usuarios:
    for usuario in usuarios:
        if usuario == 'adm':
            print(f'Olá {usuario}, gostaria de ver um relatório de status?')
        else:
            print(f'Olá {usuario}')
else:
    print('Precisamos encontrar alguns usuários')

usuarios = ['heitor', 'jose', 'adm', 'gustavo', 'marcelo']

if usuarios:
    for usuario in usuarios:
        if usuario == 'adm':
            print(f'Olá {usuario}, gostaria de ver um relatório de status?')
        else:
            print(f'Olá {usuario}')
else:
    print('Precisamos encontrar alguns usuários')


new_users = ['MARCELO', 'josaldo', 'ygor', 'Jose', 'carlos']

for user in new_users:
    if user.lower() in usuarios:
        print(f'O usuário {user} já existe')
    else:
        print(f'O nome {user} está disponível')


numbers = [1,2,3,4,5,6,7,8,9]

for number in numbers:
    if number == 1:
        print('Termina em st\n')
    elif number == 2:
        print('Termina em nd\n')
    elif number == 3:
        print('Termina em rd\n')
    else:
        print('Termina em th\n')

    