from django.contrib.auth.models import User
from django.db import models



# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=79)  # varchar
    icon = models.ImageField(upload_to='static/categories/', null=True, blank=True)  # varchar + fisier in folderul static

    def __str__(self):
        return f'{self.name}'

class Product(models.Model):
    name = models.CharField(max_length=79)  # varchar
    description = models.TextField()  # text
    price = models.DecimalField(max_digits=10, decimal_places=2)  # decimal
    stock = models.IntegerField()  # int
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE)  # int + foreign key + stergi categoria, stergi si produsele
    image = models.ImageField(upload_to='static/products', null=True, blank=True)  # varchar + fisier in folderul static


    def __str__(self):
        return f'{self.stock} X {self.name} @ {self.price}'

class Cart(models.Model):
    CART_STATUSES = (
        ('open', 'Deschis'),
        ('closed', 'Inchis')
    )
    status = models.CharField(max_length=30, choices=CART_STATUSES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
       return f'{self.status } cart of {self.user}'

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.quantity} X {self.product.name} in {self.cart}'