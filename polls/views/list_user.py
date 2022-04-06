# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView

from polls.models import UserModel
from django.db.models import Q
from polls.serializers import UserSerializer


class ListUser(APIView):  # 查看租户和房东

    def get(self, requests):
        user_obj = UserModel.objects.filter(~Q(type=0))
        item_list = []
        for item in user_obj:
            item_dict = {
                'name': item.name,
                'phone_number': item.phone_number,
                'type': '房东' if item.type == 1 else '租户',
            }
            item_list.append(item_dict)
        return Response({'info': item_list})
