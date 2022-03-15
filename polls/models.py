from django.db import models


# Create your models here.

class UserModel(models.Model):
    user_id = models.IntegerField(max_length=10, primary_key=True)
    name = models.CharField(max_length=32)
    phone_number = models.IntegerField(max_length=13)
    account = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    type = models.IntegerField(max_length=32)

    class Meta:
        db_table = "user"


class HouseInfoModel(models.Model):
    house_id = models.IntegerField(max_length=10, primary_key=True)
    house_img = models.CharField(max_length=32)
    house_area = models.CharField(max_length=32)
    house_location = models.CharField(max_length=32)
    house_type = models.IntegerField(max_length=10)
    user_id = models.IntegerField(max_length=10)
    price = models.FloatField(max_length=10)

    class Meta:
        db_table = "house_info"


class OrderInfoModel(models.Model):
    order_id = models.IntegerField(max_length=10)
    house_id = models.IntegerField(max_length=10)
    user_id = models.IntegerField(max_length=10)

    class Meta:
        db_table = "order_info"
