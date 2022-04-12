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
        user_id = requests.GET.get('user_id')
        start_time = requests.GET.get('start_time')
        end_time = requests.GET.get('end_time')

        order_obj = OrderInfoModel.objects.filter(). \
            values('house__user__name', 'order_amount', 'date', 'house_id', 'user_id')

        if user_id == 1:
            pass

        order_obj = order_obj.filter(house__user__user_id=user_id) if user_id else order_obj
        order_obj = order_obj.filter(date__gt=start_time,
                                     date__lte=end_time)  # 时间区间 大于start_time 小于end_time

        item_list = []
        tmp_list = []
        for item in order_obj:
            date_time = item.get('date').strftime('%Y-%m-01')
            args = {
                'house_user_name': item.get('house__user__name'),  # 房东
                'order_amount': item.get('order_amount'),  # 房租
                'date': date_time,
                'house_num': 1,
                'user_num': 1
            }
            if date_time not in tmp_list:
                item_list.append(args)
                tmp_list.append(date_time)
            else:
                item_list[tmp_list.index(date_time)].update({
                    'order_amount': item_list[tmp_list.index(date_time)]['order_amount'] + args['order_amount'],
                    'user_num': item_list[tmp_list.index(date_time)]['user_num'] + 1,
                    'house_num': item_list[tmp_list.index(date_time)]['house_num'] + 1
                })
        tem_date_list = []
        tem_order_amount_list = []
        tem_user_list = []
        if item_list:
            for item in item_list:
                tem_date_list.append(item['date'])
                tem_order_amount_list.append(item['order_amount'])
                tem_user_list.append(item['user_num'])

        return Response({'info': {
            'date': tem_date_list,
            'order_amount': tem_order_amount_list,
            'user_num': tem_user_list
        }})
