from django.db import models

class REGISTER(models.Model):
    user_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email_id=models.CharField(max_length=100)
    department_name=models.CharField(max_length=100)
    password=models.CharField(max_length=100)


class LOGIN_DETAILS(models.Model):
    email_id=models.CharField(max_length=100)
    password=models.CharField(max_length=100)


class FILES1(models.Model):
    file_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    image=models.ImageField(upload_to='static/uploads/')

class TEMP_FILES(models.Model):
    file_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    image=models.ImageField(upload_to='static/uploads/')
# Create your models here.
