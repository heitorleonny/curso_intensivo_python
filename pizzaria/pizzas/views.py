from django.shortcuts import render
from pizzas.models import Pizza

def index(request):
    objetos = Pizza.objects.order_by('name')
    pizzas = {'pizzas': objetos}
    return render(request, 'pizzas/index.html', pizzas)

def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.order_by('name')
    opcoes = {'pizza': pizza, 'toppings': toppings}
    
    return render(request, 'pizzas/pizza.html', opcoes)


    