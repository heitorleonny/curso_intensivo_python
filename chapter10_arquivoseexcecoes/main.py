"""with open('pi.txt') as file_object:  #with faz com que o arquivo seja fechado após utilizado
    contents = file_object.read()

print(contents)

with open('pi.txt') as file_object:
    for line in file_object:
        print(line)

with open('pi.txt') as file_object:  #armazena cada linha como intem de lista
    contents = file_object.readlines()

print(contents)

pi_string = ''
with open('pi.txt') as file_object:
    for line in file_object:
        pi_string += line.rstrip()

print(pi_string + f' Contém {len(pi_string)} caracteres')

birthday = input('Insira seu aniversário no formato ddmmyy:')

if birthday in pi_string:
    print('Seu aniversário está nos primeiros 30 dígitos de pi')
else:
    print('Seu aniversário não aparece nos primeiros 30 dígitos de pi')

arquivo = 'em_python.txt'

with open(arquivo) as file:
    dados = file.read()

print(dados)

with open(arquivo) as file:
    for line in file:
        print(line)

arquivo_string = ''
with open(arquivo) as file:
    for line in file:
        arquivo_string += line
print(arquivo_string)


with open(arquivo) as file:
    dados = file.read().replace('Python', 'C')
print(dados)

filename = 'programming.txt'

with open(filename, 'w') as file_object: # w para escreever r para ler a para concatenação e r+ para ler e escrever
    file_object.write('I love programming.\n') # importante usar quebras de linha

with open(filename, 'a') as file_object:
    file_object.write('I also love finding meaning in large datasets.\n')
    file_object.write('I love creating apps that can run in a browser.\n')


convidados = 'guest.txt'
with open(convidados, 'w') as file_object:
    nome = input('Qual o seu nome?')
    file_object.write(nome)
lista_de_convidados = 'guest_book.txt'
with open(lista_de_convidados, 'w') as file_object:
    file_object.write('É um prazer convidar vocês para o evento!\n')
    c = 0
    while c < 5:
        nome = input('Qual o seu nome?')
        file_object.write(nome + '\n')
        c += 1"""

enquete = 'enquete.txt'
with open(enquete, 'w') as file_object:
    file_object.write('Motivos para gostar de programação:\n')
    c = 0
    while c < 5:
        motivo = input('Digite um motivo pelo qual você gosta de programação:')
        file_object.write(f'{motivo}\n')
        c += 1



