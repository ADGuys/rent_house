# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView

from polls.models import UserModel
from django.db.models import Q
from polls.serializers import UserSerializer
from rent_house import settings


class UserLogin(APIView):  # 登陆

    def get(self, requests):
        account = requests.GET.get('account')
        password = requests.GET.get('password')

        user_obj = UserModel.objects.filter(account=account).values('password', 'user_id', 'type', 'user_img').first()
        if not user_obj:
            return Response({'info': '请先注册'})

        else:
            if user_obj['password'] == password:
                return Response({'info': {'user_id': user_obj['user_id'], 'user_type': user_obj['type'],
                                          'user_img': settings.STATIC_URL + (
                                              user_obj['user_img'] if user_obj['user_img'] else '')}})
            else:
                return Response({'info': '密码错误'})
