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