# Create your views here.1111
#
import datetime
import json
from dateutil import rrule

from rest_framework.response import Response
from rest_framework.views import APIView

from polls.models import OrderInfoModel, UserModel, HouseInfoModel
from django.db.models import Q, F


class ListOrder(APIView):  # 订单明细

    def get(self, requests):
        # house_id = requests.GET.get('house_id')
        user_id = requests.GET.get('user_id')
        rent_user_id = requests.GET.get('rent_user_id')

        order_obj = OrderInfoModel.objects.filter(). \
            values('user__name', 'house__house_location', 'house__house_number', 'order_type', 'rent_type',
                   'house__house_price', 'start_time', 'end_time', 'house__user__name', 'order_id', 'return_time',
                   'house_id')

        order_obj = order_obj.filter(user__user_id=user_id) if user_id else order_obj
        order_obj = order_obj.filter(house__user__user_id=rent_user_id) if rent_user_id else order_obj

        item_list = []

        for item in order_obj:
            if item.get('order_type') == 2:
                rent_type = '拒绝'
            elif item.get('order_type') == 1:
                rent_type = '申请中'
            elif item.get('order_tpye') == 3:
                rent_type = '同意退租'
            else:
                rent_type = '无申请'
            item_dict = {
                'house_location': item.get('house__house_location'),
                'house_number': item.get('house__house_number'),
                'user_name': item.get('user__name'),
                'house_user_name': item.get('house__user__name'),
                'start_time': item.get('start_time'),
                'end_time': item.get('end_time'),
                'return_time': item.get('return_time'),
                'order_type': '合同生效' if item.get('order_type') else '已退租',
                'rent_type': rent_type,
                'order_id': item.get('order_id'),
                'house_id': item.get('house_id')
            }
            start_time = datetime.datetime.strptime(str(item.get('start_time'))[:10], '%Y-%m-%d')
            end_time = datetime.datetime.strptime(str(item.get('end_time'))[:10], '%Y-%m-%d')
            months = rrule.rrule(rrule.MONTHLY, dtstart=start_time, until=end_time).count()
            item_dict.update({'house_price': (months - 1) * item.get('house__house_price')})
            item_list.append(item_dict)
        return Response({'info': item_list})

    def post(self, requests):
        order_id = requests.POST.get('order_id')
        return_type = requests.POST.get('return_type')  # 2拒绝 3同意
        house_id = requests.POST.get('house_id')
        return_type_up = requests.POST.get('return_type_up')  # 提交

        order_obj = OrderInfoModel.objects.filter(order_id=order_id)
        house_obj = HouseInfoModel.objects.filter(house_id=house_id)

        order_obj.update(order_type=return_type) if return_type else None
        if return_type:
            order_obj.update(return_time=datetime.datetime.now()) if return_type == 3 else None
            house_obj.update(house_type=0) if return_type == 3 else None
            if int(return_type) == 2:
                return Response({'info': '拒绝退租'})
            if int(return_type) == 3:
                return Response({'info': '同意退租'})
        return Response({'info': ''})
