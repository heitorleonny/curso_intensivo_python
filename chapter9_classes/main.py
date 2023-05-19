"""class Restaurant():
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'O nome do restaurante é {self.name.title()} e eles servem {self.cuisine_type}.')

    def open_restaurant(self):
        print(f'O restaurante {self.name} está aberto!')


restaurante1 = Restaurant('Dona Muchacha', 'comida mexicana')
restaurante2 = Restaurant('Mac Donalds', 'fast food')
restaurante3 = Restaurant('Masayuki', 'comida japonesa')

restaurante1.describe_restaurant()
restaurante2.describe_restaurant()
restaurante3.describe_restaurant()


class User():
    def __init__(self, first_name, last_name, sex, age ):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age

    def describe_user(self):
        print(f'Primeiro nome: {self.first_name.title()}\nSobrenome: {self.last_name.title()}\nIdade: {self.age}\nSexo: {self.sex}')

    def greet_user(self):
        print(f'Muito bom ter você aqui, {self.first_name.title()} {self.last_name.title()}')

user1 = User('Heitor', 'Leonny', 'masculino', '18')


user1.describe_user()
user1.greet_user()


user2 = User('José', 'Ronaldo', 'masculino', '38')


user2.describe_user()
user2.greet_user()

class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 23

    def get_descriptive_name(self):
        print(f'O carro é o {self.make} {self.model} {self.year}')

    def read_odometer(self):
        print(f'A quilometragem do carro é {self.odometer_reading}km')

    def update_odometer(self, quilometragem):
        if quilometragem >= self.odometer_reading:
            self.odometer_reading = quilometragem
        else:
            print('Você não poder reverter um hodômetro')

my_car = Car('Audi', 'A4', 2016)

my_car.get_descriptive_name()
my_car.read_odometer()
my_car.update_odometer(22)
my_car.read_odometer()


class Restaurant():
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.numbed_server = 50

    def describe_restaurant(self):
        print(f'O nome do restaurante é {self.name.title()} e eles servem {self.cuisine_type}.')

    def open_restaurant(self):
        print(f'O restaurante {self.name} está aberto!')

    def clientes(self):
        print(f'O número de clientes atendidos até o momento foi {self.numbed_server}')

    def increment_mumber_served(self, clientes):
        self.numbed_server += clientes




restaurante = Restaurant('Dona Muchacha', 'comida mexicana')

restaurante.clientes()
restaurante.increment_mumber_served(40)
restaurante.clientes()

class User():
    def __init__(self, first_name, last_name, sex, age ):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print(f'Primeiro nome: {self.first_name.title()}\nSobrenome: {self.last_name.title()}\nIdade: {self.age}\nSexo: {self.sex}')

    def greet_user(self):
        print(f'Muito bom ter você aqui, {self.first_name.title()} {self.last_name.title()}')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user1 = User('Heitor', 'Leonny', 'masculino', '18')
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)


class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 23

    def get_descriptive_name(self):
        print(f'O carro é o {self.make} {self.model} {self.year}')

    def read_odometer(self):
        print(f'A quilometragem do carro é {self.odometer_reading}km')

    def update_odometer(self, quilometragem):
        if quilometragem >= self.odometer_reading:
            self.odometer_reading = quilometragem
        else:
            print('Você não poder reverter um hodômetro')

my_car = Car('Audi', 'A4', 2016)


class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f'This car has a {self.battery_size}kwh battery')

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = f'This car can go approximately {str(range)} miles on a full charge'
        print(message)


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()



my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())
print(my_tesla.battery.describe_battery())
print(my_tesla.battery.get_range())




class Restaurant():
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.numbed_server = 50

    def describe_restaurant(self):
        print(f'O nome do restaurante é {self.name.title()} e eles servem {self.cuisine_type}.')

    def open_restaurant(self):
        print(f'O restaurante {self.name} está aberto!')

    def clientes(self):
        print(f'O número de clientes atendidos até o momento foi {self.numbed_server}')

    def increment_mumber_served(self, clientes):
        self.numbed_server += clientes


class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.flavors = 'Chocolate, Morango, Abacaxi, Limão, Coco, Açaí, Uva'

    def listar_sabores(self):
        print(self.flavors)

sorveteria = IceCreamStand('Sorveteria do chico', 'sorvetes')
print(sorveteria.describe_restaurant())
sorveteria.listar_sabores()


class User():
    def __init__(self, first_name, last_name, sex, age ):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print(f'Primeiro nome: {self.first_name.title()}\nSobrenome: {self.last_name.title()}\nIdade: {self.age}\nSexo: {self.sex}')

    def greet_user(self):
        print(f'Muito bom ter você aqui, {self.first_name.title()} {self.last_name.title()}')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Privilleges():
    def __init__(self):
        self.privilleges = 'privilégios:\ncan add post\ncan delete post\ncan ban user'


    def show_privilleges(self):
        print(self.privilleges)


class Admin(User):
    def __init__(self, first_name, last_name, sex, age):
        super(Admin, self).__init__(first_name, last_name, sex, age)
        self.privilleges = Privilleges()




adm1 = Admin('Heitor', 'Leonny', 'masculino', 18)
adm1.describe_user()
adm1.privilleges.show_privilleges()"""


class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 23

    def get_descriptive_name(self):
        print(f'O carro é o {self.make} {self.model} {self.year}')

    def read_odometer(self):
        print(f'A quilometragem do carro é {self.odometer_reading}km')

    def update_odometer(self, quilometragem):
        if quilometragem >= self.odometer_reading:
            self.odometer_reading = quilometragem
        else:
            print('Você não poder reverter um hodômetro')

my_car = Car('Audi', 'A4', 2016)


class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f'This car has a {self.battery_size}kwh battery')

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = f'This car can go approximately {str(range)} miles on a full charge'
        print(message)

    def upgrade_battery(self):
        if self.battery_size == 70:
            self.battery_size = 85
            print('A bateria foi melhorada')
        elif self.battery_size == 85:
            print('A bateria já está na potência máxima')


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()



my_tesla = ElectricCar('tesla', 'model s', 2016)

my_tesla.get_descriptive_name()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()










