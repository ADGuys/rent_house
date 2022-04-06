import datetime
import json
from dateutil import rrule

from rest_framework.response import Response
from rest_framework.views import APIView

from polls.models import OrderInfoModel, UserModel, HouseInfoModel
from django.db.models import Q, F


class InsertOrderDetail(APIView):
    def post(self, requests):
        user_id = requests.POST.get('user_id')  # 用户ID
        house_city = requests.POST.get('house_city')  # 房屋所在城市
        house_location = requests.POST.get('house_location')  # 房屋所在地理位置
        house_number = requests.POST.get('house_number')  # 房屋门牌号
        house_rent_type = requests.POST.get('house_rent_type')  # 房屋租赁类型
        house_area = requests.POST.get('house_area')  # 房屋面积
        house_price = requests.POST.get('house_price')  # 租赁价格
        bedroom_number = requests.POST.get('bedroom_number')  # 卧室数量
        bathroom_number = requests.POST.get('bathroom_number')  # 洗手间数量
        house_detail = requests.POST.get('house_detail')  # 房屋明细
        house_img = requests.FILES.get('house_img', None)  # 房屋图片


