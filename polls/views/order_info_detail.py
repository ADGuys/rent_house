# Create your views here.1
#
import datetime
import json
from dateutil import rrule

from rest_framework.response import Response
from rest_framework.views import APIView

from polls.models import OrderInfoModel, UserModel, HouseInfoModel


class ListOrderDetail(APIView):  # 订单明细

    def get(self, requests):
        rent_user_id = requests.GET.get('rent_user_id')

        order_obj = OrderInfoModel.objects.filter(). \
            values('house__user__name', 'house__house_price', 'return_time', 'order_type', 'start_time', 'end_time')

        order_obj = order_obj.filter(house__user__user_id=rent_user_id) if rent_user_id else order_obj

        item_list = []
        order_count = 0
        for item in order_obj:
            order_count += 1
            start_time = datetime.datetime.strptime(str(item.get('start_time'))[:10], '%Y-%m-%d')  # 转为datetime做时间处理
            end_time = datetime.datetime.strptime(str(item.get('end_time'))[:10], '%Y-%m-%d')
            return_time = datetime.datetime.strptime(str(item.get('return_time'))[:10], '%Y-%m-%d') if item.get(
                'return_time') else 0
            


            item_dict = {
                'order_count': order_count,  # 租客数量
                'house_number': 1,
                'user_name': item.get('user__name'),
                'house_user_name': item.get('house__user__name'),
                'start_time': item.get('start_time'),
                'end_time': item.get('end_time'),
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
