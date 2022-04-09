# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView

from polls.models import UserModel
from django.db.models import Q
from polls.serializers import UserSerializer


class ListUser(APIView):  # 查看租户和房东

    def get(self, requests):
        user_id = requests.GET.get('user_id')

        user_obj = UserModel.objects.filter()
        if user_id:
            user_obj = user_obj.filter(user_id=user_id)
        item_list = []
        for item in user_obj:
            if item.type == 0:
                user_type = '管理员'
            elif item.type == 1:
                user_type = '房东'
            else:
                user_type = '租户'
            item_dict = {
                'name': item.name,
                'phone_number': item.phone_number,
                'user_info': item.info,
                'type': user_type,
                'account': item.account,
                'date': item.date,
                'user_img': item.user_img
            }
            item_list.append(item_dict)
        return Response({'info': item_list})

    def post(self, requests):
        user_id = requests.GET.get('user_id')
        name = requests.GET.get('name')
        phone_number = requests.GET.get('phone_number')
        account = requests.GET.get('account')
        password = requests.GET.get('password')
        date = requests.GET.get('date')
        info = requests.GET.get('info')
        user_img = requests.FILES.get('user_img')

        user_ojb = UserModel.objects.filter(user_id=user_id)
        user_ojb.update(name=name) if name else None
        user_ojb.update(phone_number=phone_number) if phone_number else None
        user_ojb.update(account=account) if account else None
        user_ojb.update(password=password) if password else None
        user_ojb.update(date=date) if date else None
        user_ojb.update(info=info) if info else None
        user_ojb.update(user_img=user_img.name) if user_img else None
        if user_img:
            save_path = '/Users/loctek/PycharmProjects/rent_house/static/{}'.format(user_img.name)
            with open(save_path, 'wb') as f:
                for content in user_img.chunks():
                    f.write(content)

        return Response({'info': '修改成功'})
