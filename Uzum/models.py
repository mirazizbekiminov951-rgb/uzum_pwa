from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, null=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', null=True)
    rasm = models.ImageField(upload_to='media/')
    nomi = models.CharField(max_length=50)
    narxi = models.IntegerField()
    skidka = models.IntegerField()
    rate = models.FloatField(null=True)
    is_aksiya = models.BooleanField(default=False)
    is_arzonlashdi = models.BooleanField(default=False)
    tavsif = models.TextField(null=True)
    def __str__(self):
        return self.nomi