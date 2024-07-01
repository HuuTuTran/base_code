from django.contrib import admin
from products import models
admin.site.register(models.products)
admin.site.register(models.manufacturer)