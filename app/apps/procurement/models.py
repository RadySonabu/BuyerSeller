from django.db import models

# Create your models here.
class Buyer(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Seller(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    selling_price_per_kg = models.FloatField()

    def __str__(self):
        return self.name
    
class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('Buy', 'Buy'),
        ('Sell', 'Sell'),
    )
    transaction_type = models.CharField(max_length=50, choices=TRANSACTION_TYPES)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity_in_kg = models.FloatField()
    amount = models.FloatField()

    def __str__(self):
        return str(self.transaction_type)
    
    