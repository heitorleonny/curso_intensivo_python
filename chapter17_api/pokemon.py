import requests
n = 1
while n <= 151:
    pokemons = requests.get(f'https://pokeapi.co/api/v2/pokemon/{str(n)}/').json()
    print(pokemons['name'], pokemons['base_experience'])
    n += 1