"""filename = 'alce.txt'
new_name = 'alice.txt'
try:

    with open(filename, 'r') as file_object:
        contents = file_object.read()

except FileNotFoundError:
    print(f'O arquivo {filename} não existe')
else:
    words = contents.split()
    num_words = len(words)
    print(f'The file {filename} has about {str(num_words)} {words}')

try:

    with open(new_name, 'r') as file_object:
        contents = file_object.read()
except:
    pass
else:
    words = contents.split()
    num_words = len(words)
    print(f'The file {new_name} has about {str(num_words)} {words}')

x = 0
y = 0
while True:
    x = input('n1')
    y = input('n2')
    if x == 'q' or y == 'q':
        break
    else:

        try:
            soma = int(x) + int(y)
        except ValueError:
            print('Apenas números são aceitos!')
        else:
            print(f'A soma é {soma}')"""


dogs = 'dos.txt'
cats = 'cats.txt'

try:
    with open(dogs) as file_object:
        contentes = file_object.read()

except FileNotFoundError:
    pass
else:
    print(contentes)

try:
    with open(cats) as file_object:
        contentes = file_object.read()

except FileNotFoundError:
    print(f'O arquivo {cats} não existe.')
else:
    print(contentes)


with open('programming.txt') as file_object:
    arquivo = file_object.read()

print('A palvra "love" aparece:')
print(arquivo.lower().count('love') , 'vezes' )



















        























