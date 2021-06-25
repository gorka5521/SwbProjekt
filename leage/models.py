from django.db import models


# Create your models here.

class Rola(models.Model):
    nazwa = models.TextField(max_length=50)

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name = "Rola"
        verbose_name_plural = "Role"


class Pozycja(models.Model):
    nazwa = models.TextField(max_length=50)

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name = "Pozycja"
        verbose_name_plural = "Pozycje"


class Postac(models.Model):
    nazwa = models.CharField(max_length=100)
    opis = models.CharField(max_length=2000)
    rola = models.ForeignKey(Rola, on_delete=models.CASCADE, null=True)
    pozycja = models.ForeignKey(Pozycja, on_delete=models.CASCADE, null=True)
    kod = models.CharField(max_length=10)

    nazwaP = models.CharField(max_length=100)
    opisP = models.CharField(max_length=500)

    nazwaQ = models.CharField(max_length=100)
    opisQ = models.CharField(max_length=500)

    nazwaW = models.CharField(max_length=100)
    opisW = models.CharField(max_length=500)

    nazwaE = models.CharField(max_length=100)
    opisE = models.CharField(max_length=500)

    nazwaR = models.CharField(max_length=100)
    opisR = models.CharField(max_length=500)

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name = "Postać"
        verbose_name_plural = "Postacie"


class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Out Door', 'Out Door'),
    )

    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )

    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    note = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.product.name
