# Create your views here.1
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
                   'house__house_price', 'start_time', 'end_time', 'house__user__name', 'order_id', 'return_time')

        order_obj = order_obj.filter(user__user_id=user_id) if user_id else order_obj
        order_obj = order_obj.filter(house__user__user_id=rent_user_id) if rent_user_id else order_obj

        item_list = []
        for item in order_obj:
            item_dict = {
                'house_location': item.get('house__house_location'),
                'house_number': item.get('house__house_number'),
                'user_name': item.get('user__name'),
                'house_user_name': item.get('house__user__name'),
                'start_time': item.get('start_time'),
                'end_time': item.get('end_time'),
                'return_time': item.get('return_time'),
                'order_type': '合同生效' if item.get('order_type') else '已退租',
                'rent_type': '申请中' if item.get('rent_type') else '退租申请',
                'order_id': item.get('order_id'),
            }
            start_time = datetime.datetime.strptime(str(item.get('start_time'))[:10], '%Y-%m-%d')
            end_time = datetime.datetime.strptime(str(item.get('end_time'))[:10], '%Y-%m-%d')
            months = rrule.rrule(rrule.MONTHLY, dtstart=start_time, until=end_time).count()
            item_dict.update({'house_price': (months - 1) * item.get('house__house_price')})
            item_list.append(item_dict)
        return Response({'info': item_list})

    def post(self, requests):
        start_time = requests.POST.get('start_time')
        end_time = requests.POST.get('end_time')
        house_id = requests.POST.get('house_id')
        order_id = requests.POST.get('order_id')
        status = requests.POST.get('status')  # 1添加，2删除，3更新

        if status == '1':
            house_obj = HouseInfoModel.objects.filter(house_id=house_id).values('user__user_id').first()
            order_ojb = OrderInfoModel()
            print(house_obj['user__user_id'], 312)
            order_item = {
                'start_time': start_time,
                'end_time': end_time,
                'house_id': int(house_id),
                'user_id': int(house_obj['user__user_id'])
            }
            print(order_ojb, 123)
            OrderInfoModel().save()
            return Response({'info': '成功下单'})
            pass
        house_obj = HouseInfoModel.objects.filter(house_id=house_id).values('user__user_id')
        return Response({'info': ''})
