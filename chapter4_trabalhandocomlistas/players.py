players = ['charles', 'martina', 'michael', 'florence', 'eli', 'neymar', 'messi', 'cr7', 'pedro']
print(players[0:3])
print(players[-3:])

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player)

print('Os 3 jogadores do meio do meu time são:')
for player in players[3:6]:
    print(player)

print('Os 3 últimos jogadores são:')
for player in players[-3:]:
    print(player)

