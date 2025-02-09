from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name 

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(max_length=100)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class ProductTree(models.Model):
    ancestor = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='descendants')
    descendant = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ancestors')
class Order(models.Model):
    ref_no = models.CharField(max_length=100)    
    date_created = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders', null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    def __str__(self):
        return self.ref_no



