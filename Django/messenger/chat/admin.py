from django.contrib import admin
from chat import models
# Register your models here.
admin.site.register(models.users)
admin.site.register(models.user_relations)
admin.site.register(models.messengers)
admin.site.register(models.group)
admin.site.register(models.members)
