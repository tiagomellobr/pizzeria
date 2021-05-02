from django.db import models


class Flavor(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField()

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name


class Pizza(models.Model):
    quantity = models.IntegerField()
    flavor = models.ForeignKey(Flavor, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)

    def __str__(self):
        return "%s (%s), qty: %s" % (self.flavor.name, self.size.name, self.quantity)


class Customer(models.Model):
    full_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=45)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=45)
    state_province = models.CharField(max_length=45, null=True)
    country = models.CharField(max_length=45)
    postal_code = models.CharField(max_length=45)

    def __str__(self):
        return self.full_name


class OrderStatus(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name


class Order(models.Model):
    note = models.TextField(null=True)
    status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    pizza = models.ManyToManyField(Pizza)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.pk
