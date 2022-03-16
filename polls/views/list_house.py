# Create your views here.1

from rest_framework.response import Response
from rest_framework.views import APIView

from polls.models import HouseInfoModel, UserModel
from django.db.models import Q


class ListHouse(APIView):  # 查看房屋

    def get(self, requests):
        house_obj = HouseInfoModel.objects.filter()

        item_list = []
        for item in user_obj:
            item_dict = {
                'name': item.name,
                'phone_number': item.phone_number,
                'type': '房东' if item.type == 1 else '租户',
            }
            item_list.append(item_dict)
        return Response({'info': item_list})
