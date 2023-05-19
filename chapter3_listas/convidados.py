convidados = ['Messi', 'Cristiano Ronaldo', 'Neymar']

print(f'Olá {convidados[0]}! Você está convidado para o jantar!')
print(f'Olá {convidados[1]}! Você está convidado para o jantar!')
print(f'Olá {convidados[2]}! Você está convidado para o jantar!')

print(f'Infelizmente {convidados[1]} não podera aparecer.')

convidados = ['Messi', 'Casemiro', 'Neymar']

print(f'Olá {convidados[0]}! Você está convidado para o jantar!')
print(f'Olá {convidados[1]}! Você está convidado para o jantar!')
print(f'Olá {convidados[2]}! Você está convidado para o jantar!')

print('Opa!!! A mesa é maior do que o esperado, nesse caso também chamarei Anthony, Raphinha e Richarlison')

convidados.insert(0, 'Anthony')
convidados.insert(3, 'Raphinha')
convidados.append('Richarlison')

print(f'Olá {convidados[0]}! Você está convidado para o jantar!')
print(f'Olá {convidados[1]}! Você está convidado para o jantar!')
print(f'Olá {convidados[2]}! Você está convidado para o jantar!')
print(f'Olá {convidados[3]}! Você está convidado para o jantar!')
print(f'Olá {convidados[4]}! Você está convidado para o jantar!')
print(f'Olá {convidados[5]}! Você está convidado para o jantar!')


print('#' *50)
print('Infelizmente a mesa não vai chegar a tempo e apenas duas pessoas poderão ser convidadas.')

print(f'Sinto muito {convidados[-1]} mas você não está mais convidado para o jantar.')
convidados.pop()
print(f'Sinto muito {convidados[-1]} mas você não está mais convidado para o jantar.')
convidados.pop()
print(f'Sinto muito {convidados[-1]} mas você não está mais convidado para o jantar.')
convidados.pop()
print(f'Sinto muito {convidados[-1]} mas você não está mais convidado para o jantar.')
convidados.pop()


print(f'Olá {convidados[0]}! Você está convidado para o jantar!')
print(f'Olá {convidados[1]}! Você está convidado para o jantar!')

del[convidados[0]]
del[convidados[0]]

print(convidados)
