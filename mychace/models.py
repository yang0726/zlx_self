from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=200)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=50)

    class Meta:
        db_table = 'm_user'
