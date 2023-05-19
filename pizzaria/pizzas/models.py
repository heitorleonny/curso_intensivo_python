from django.db import models

class Pizza(models.Model):
    name = models.TextField()
    
    def __str__(self):
        return self.name
    
class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.TextField()
    
    class Meta:
        verbose_name_plural = 'Toppings'
    
    def __str__(self):
        return self.name
