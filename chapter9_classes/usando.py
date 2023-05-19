from restaurant import Restaurant
from admin import Admin

sorveteria = Restaurant('Sorveteria do chico', 'sorvetes')
sorveteria.describe_restaurant()
adm1 = Admin('Heitor', 'Leonny', 'masculino', 18)
adm1.describe_user()
adm1.privilleges.show_privilleges()