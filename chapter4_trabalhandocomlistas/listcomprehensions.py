squares = [value**2 for value in range(1,101)]
print(squares)


numbers = [number for number in range(1,1000001)]
print(min(numbers))
print(max(numbers))
print(sum(numbers))


for impar in range(1,21, 2):
    print(impar)
print('#'*50)
for multiplo in range(3,31,3):
    print(multiplo)
print('#'*50)
for cubo in range(1,11):
    print(cubo**3)
print('#'*50)


cubos = [number**3 for number in range(1,11)]
print(cubos)