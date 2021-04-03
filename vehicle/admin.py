from django.contrib import admin
from .models import Car, Cost, Sales
# Register your models here.
admin.site.register(Cost)
admin.site.register(Car)
admin.site.register(Sales)