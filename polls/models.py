from django.db import models
from rest_framework.pagination import PageNumberPagination


class PageNumberPagination(PageNumberPagination):  # 分页器
    page_query_param = "page"
    page_size_query_param = 'page_size'  # 前端收到页面的关键字名称，默认是page
    max_page_size = 8  # 每页数据个数


class UserModel(models.Model):
    user_id = models.IntegerField(max_length=10, primary_key=True)
    name = models.CharField(max_length=32)
    phone_number = models.IntegerField(max_length=13)
    account = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    type = models.IntegerField(max_length=32)
    date = models.DateTimeField()

    class Meta:
        db_table = "user"


class HouseInfoModel(models.Model):
    house_id = models.IntegerField(max_length=10, primary_key=True)
    house_img = models.CharField(max_length=32)
    house_area = models.IntegerField(max_length=32)
    house_province = models.CharField(max_length=32)
    house_city = models.CharField(max_length=32)
    house_location = models.CharField(max_length=32)
    house_number = models.CharField(max_length=32)
    house_type = models.IntegerField(max_length=10)
    house_rent_type = models.IntegerField(max_length=10)
    user = models.ForeignKey("UserModel", on_delete=models.CASCADE)
    # user_id = models.IntegerField(max_length=10)
    house_price = models.FloatField(max_length=10)
    bedroom_number = models.IntegerField(max_length=10)
    bathroom_number = models.IntegerField(max_length=10)
    house_detail = models.TextField(max_length=1000)
    date = models.DateTimeField()
    is_delete = models.IntegerField(max_length=10)

    # pagination_class = CarPageNumberPagination()
    # page_obj = pagination_class.paginate_queryset(book, request)  # 进行分页

    class Meta:
        db_table = "house_info"


class OrderInfoModel(models.Model):
    order_id = models.IntegerField(max_length=10, primary_key=True)
    house = models.ForeignKey("HouseInfoModel", on_delete=models.CASCADE)
    user = models.ForeignKey("UserModel", on_delete=models.CASCADE)
    order_type = models.IntegerField(max_length=10)
    rent_type = models.IntegerField(max_length=10)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    return_time = models.DateTimeField()
    date = models.DateTimeField()

    class Meta:
        db_table = "order_info"
