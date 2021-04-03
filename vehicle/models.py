from django.db import models

# Create your models here.
class Car(models.Model):
    make = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    yom = models.DateField()
    created_at = models.DateTimeField()
    engine_no = models.CharField(max_length=100)
    chassis_number = models.CharField(max_length=100)
    reg_number = models.CharField(max_length=100, null=True)
    color = models.CharField(max_length=100)
    
    def __str__(self):
        return (self.make + self.car_model)

class Cost(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    customs = models.IntegerField()
    cif_cost = models.IntegerField()
    delivery_order = models.IntegerField()
    radiation = models.IntegerField()
    ntsa_sticker = models.IntegerField()
    insurance = models.IntegerField()
    cfs_chgs = models.IntegerField()
    agency = models.IntegerField()
    total_cost = models.IntegerField()

    def __str__(self):
        return str(self.total_cost)

class Sales(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    selling_price = models.IntegerField()
    total_cost = models.ForeignKey(Cost, on_delete=models.CASCADE)
    profit = models.IntegerField()
    
    def __str__(self):
        return str(self.profit)
    