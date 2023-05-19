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