# Create your views here.1
# 还需要关联添加一些房屋信息
import datetime

from rest_framework.response import Response
from rest_framework.views import APIView

from polls.models import HouseInfoModel, UserModel, PageNumberPagination, OrderInfoModel
from rent_house import settings


class InsertOrder(APIView):  # 插入订单

    def post(self, requests):
        user_id = requests.POST.get('user_id')
        house_id = requests.POST.get('house_id')
        start_time = requests.POST.get('start_time')
        end_time = requests.POST.get('end_time')
        order_amount = requests.POST.get('order_amount')

        house_obj = HouseInfoModel.objects.filter(house_id=house_id).first()
        if house_obj.house_type:
            return Response({'info': '房屋已经被租用'})

        order_obj = OrderInfoModel(house_id=house_id, user_id=user_id, order_type=1, start_time=start_time,
                                   end_time=end_time, rent_type=0, date=datetime.datetime.now(),
                                   order_amount=order_amount)
        order_obj.save()
        HouseInfoModel.objects.filter(house_id=house_id).update(house_type=1)
        return Response({'info': '下单成功'})
