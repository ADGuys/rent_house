# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView

from polls.models import UserModel
from django.db.models import Q
from polls.serializers import UserSerializer


class UserLogin(APIView):  # 登陆

    def get(self, requests):
        account = requests.GET.get('account')
        password = requests.GET.get('password')

        user_obj = UserModel.objects.filter(account=account).values('password', 'user_id', 'type').first()
        print(user_obj, 123123)
        if not user_obj:
            return Response({'info': '请先注册'})

        else:
            if user_obj['password'] == password:
                return Response({'info': {'user_id': user_obj['user_id'], 'user_type': user_obj['type']}})
            else:
                return Response({'info': '密码错误'})
