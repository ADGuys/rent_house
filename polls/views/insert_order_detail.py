import datetime
import json
import time

from dateutil import rrule

from rest_framework.response import Response
from rest_framework.views import APIView

from polls.models import OrderInfoModel, UserModel, HouseInfoModel


class InsertOrderDetail(APIView):
    def post(self, requests):
        house_id = requests.POST.get('user_id')  # 用户ID
        user_id = requests.POST.get('house_city')  # 租户ID
        start_time = requests.POST.get('house_number')  # 开始时间
        end_time = requests.POST.get('house_number')  # 开始时间

        order_obj = HouseInfoModel(house_id=house_id, user_id=user_id, start_time=start_time,
                                   end_time=end_time, date=datetime.datetime.now(),
                                   rent_type=0, order_type=1)
        order_obj.save()

        house_ojb = HouseInfoModel.objects.filter(house_id=house_id)

        return Response({'info': '成功下单'})
