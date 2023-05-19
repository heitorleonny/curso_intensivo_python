my_pizzas = ['calabresa', 'MUSSARELA', 'Frango com bacon e catupiry']

for pizza in my_pizzas:
    print(f'Eu gosto de pizza de {pizza.title()}!')
print('UAUUu! Eu realmente gosto de pizza!')


friend_pizzas = my_pizzas[:]

my_pizzas.append('3 queijos')
friend_pizzas.append('brigadeiro')

print('Eu gosto de pizza de:')
for pizza in my_pizzas:
    print(pizza)

print('Meu amigo gosta de pizza de:')
for pizza in friend_pizzas:
    print(pizza)
