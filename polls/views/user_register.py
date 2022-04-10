# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView

from polls.models import UserModel
from django.db.models import Q
from polls.serializers import UserSerializer


class UserRegister(APIView):  # 注册

    def get(self, requests):
        name = requests.GET.get('name')
        phone_number = requests.GET.get('phone_number')
        account = requests.GET.get('account')
        password = requests.GET.get('password')
        type = requests.GET.get('type')

        user_fir_obj = UserModel.objects.filter(account=account)
        if user_fir_obj:
            return Response({'info': '请更换账号名称'})

        user_obj = UserModel(name=name, phone_number=phone_number, account=account,
                             password=password, type=type)
        user_obj.save()
        return Response({'info': '注册成功'})

        # else:
        # if user_obj['password'] == password:
        #     return Response({'info': {'user_id': user_obj['user_id'], 'user_type': user_obj['type']}})
        # else:
        #     return Response({'info': '密码错误'})
