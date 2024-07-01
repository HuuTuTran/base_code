from django.db import models

# Create your models here.
class users (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)    
    pwd = models.CharField(max_length=200)
    status = models.IntegerField()
class group(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    is_group = models.BooleanField() 
    updated = models.DateTimeField()

class user_relations(models.Model):
    id = models.AutoField(primary_key=True)
    id_1 = models.IntegerField()
    id_2 = models.IntegerField()

class members(models.Model):
    id = models.AutoField(primary_key=True)
    id_group  = models.ForeignKey(group,on_delete=models.CASCADE)
    id_user  =  models.ForeignKey(users,on_delete=models.CASCADE)


class messengers(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=1000)
    id_group  = models.ForeignKey(group,on_delete=models.CASCADE)
    date = models.DateTimeField()
    sender_id = models.ForeignKey(members,on_delete=models.CASCADE)

        
