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