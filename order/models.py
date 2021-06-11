from django.db import models

# Create your models here.
from aadil.models import Clothing

class Order(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    payment = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'Order #{self.id}'

    def total_price(self):
        return sum(item.get_price() for item in self.items.all())

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete = models.CASCADE)

    product = models.ForeignKey(Clothing, related_name='order_items',on_delete=models.CASCADE)

    price = models.DecimalField(max_digits=10, decimal_places=2)

    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_price(self):
        return self.price * self. quantity