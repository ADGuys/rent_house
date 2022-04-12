# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView

from polls.models import UserModel, PageNumberPagination
from django.db.models import Q
from polls.serializers import UserSerializer
from rent_house import settings


class ListUser(APIView):  # 查看租户和房东

    def get(self, requests):
        user_id = requests.GET.get('user_id')

        user_obj_1 = UserModel.objects.filter(is_delete=1)
        if user_id:
            user_obj_1 = user_obj_1.filter(user_id=user_id)
        paginate = PageNumberPagination()
        user_obj = paginate.paginate_queryset(user_obj_1, requests)
        item_list = []
        for item in user_obj:
            if item.type == 0:
                user_type = '管理员'
            elif item.type == 1:
                user_type = '房东'
            else:
                user_type = '租户'
            item_dict = {
                'id': item.user_id,
                'name': item.name,
                'phone_number': item.phone_number,
                'user_info': item.info,
                'type': user_type,
                'account': item.account,
                'date': item.date,
                'user_img': settings.STATIC_URL + (str(item.user_img) if item.user_img else 'pc1_jSNJPBOi9.jpeg')
            }
            item_list.append(item_dict)
        return Response({'info': item_list, 'total_num': paginate.django_paginator_class(user_obj_1, 6).count})

    def post(self, requests):
        user_id = requests.POST.get('user_id')
        name = requests.POST.get('name')
        phone_number = requests.POST.get('phone_number')
        # old_password = requests.POST.get('password')
        new_password = requests.POST.get('new_password')
        info = requests.POST.get('info')
        user_img = requests.FILES.get('user_img')

        user_ojb = UserModel.objects.filter(user_id=user_id)
        user_ojb.update(password=new_password) if new_password else None

        user_ojb.update(name=name) if name else None
        user_ojb.update(phone_number=phone_number) if phone_number else None
        # print(user_ojb.get('password'), 123)

        user_ojb.update(info=info) if info else None
        user_ojb.update(user_img=user_img.name) if user_img else None
        if user_img:
            save_path = '/Users/loctek/PycharmProjects/rent_house/static/{}'.format(user_img.name)
            with open(save_path, 'wb') as f:
                for content in user_img.chunks():
                    f.write(content)

        return Response({'info': '修改成功'})

    def delete(self, requests):
        user_id = requests.GET.get('user_id')
        UserModel.objects.filter(user_id=user_id).update(is_delete=0)
        return Response({'info': '删除成功'})
