# Create your views here.1
# 还需要关联添加一些房屋信息

from rest_framework.response import Response
from rest_framework.views import APIView

from polls.models import HouseInfoModel, UserModel, PageNumberPagination
from rent_house import settings


class ListHouse(APIView):  # 查看房屋

    def get(self, requests):
        house_id = requests.GET.get('house_id')
        house_city = requests.GET.get('house_city')
        house_area = requests.GET.get('house_area')
        house_price = requests.GET.get('house_price')
        house_type = requests.GET.get('house_type')
        house_rent_type = requests.GET.get('house_rent_type')

        list_area = house_area.split(',') if house_area else []
        list_price = house_price.split(',') if house_price else []

        house_obj = HouseInfoModel.objects.filter(). \
            values('user__user_id', 'house_id', 'house_img', 'house_area', 'house_province', 'house_city',
                   'house_location', 'house_number', 'house_price', 'bedroom_number', 'bathroom_number', 'house_detail',
                   'date', 'user__name', 'user__phone_number', 'house_rent_type')

        house_obj = house_obj.filter(house_id=house_id) if house_id else house_obj  # ID
        house_obj = house_obj.filter(house_city=house_city) if house_city else house_obj  # CITY
        house_obj = house_obj.filter(house_type=house_type) if house_type else house_obj  # 类型
        house_obj = house_obj.filter(house_rent_type=house_rent_type) if house_rent_type else house_obj  # 出租类型
        house_obj = house_obj.filter(house_area__gt=int(list_area[0])) if list_area else house_obj  # 面积区间
        house_obj = house_obj.filter(house_area__lte=int(list_area[1])) if list_area and list_area[1] else house_obj

        house_obj = house_obj.filter(house_price__gt=int(list_price[0])) if list_price else house_obj  # 价格区间
        house_obj = house_obj.filter(house_price__lte=int(list_price[1])) if list_price and list_price[
            1] else house_obj  # 价格区间

        paginate = PageNumberPagination()
        house_obj = paginate.paginate_queryset(house_obj, requests)

        item_list = []
        total_page = 0
        for item in house_obj:
            total_page += 1
            # print(item, 312)
            # print(a, 321)
            # print(item['user__account'])
            # print(item.)
            item_dict = {
                'house_id': item.get('house_id'),
                'house_area': item.get('house_area'),
                'house_province': item.get('house_province'),
                'house_img': settings.STATIC_URL + item.get('house_img'),
                'house_city': item.get('house_city'),
                'house_location': item.get('house_location'),
                'house_number': item.get('house_number'),
                'house_price': item.get('house_price'),
                'bedroom_number': item.get('bedroom_number'),
                'bathroom_number': item.get('bathroom_number'),
                'house_detail': item.get('house_detail'),
                'user_name': item.get('user__name'),
                'user_phone_number': item.get('user__phone_number'),
                'house_rent_type': '合租' if item.get('user__phone_number') else '整租',
            }

            item_list.append(item_dict)
        # house_obj = UserModel.objects.filter(user__user_id=item_dict.)
        return Response({'info': item_list, 'total_page': total_page})

    def post(self, requests):
        house_id = requests.POST.get('house_id')
        house_city = requests.POST.get('house_city')
        house_location = requests.POST.get('house_location')
        house_number = requests.POST.get('house_number')
        house_rent_type = requests.POST.get('house_rent_type')
        house_area = requests.POST.get('house_area')
        house_price = requests.POST.get('house_price')
        bedroom_number = requests.POST.get('bedroom_number')
        bathroom_number = requests.POST.get('bathroom_number')
        house_detail = requests.POST.get('house_detail')
        house_img = requests.FILES.get('house_img', None)

        house_ojb = HouseInfoModel.objects.filter(house_id=house_id)

        house_ojb.update(house_city=house_city) if house_city else None
        house_ojb.update(house_location=house_location) if house_location else None
        house_ojb.update(house_number=house_number) if house_number else None
        house_ojb.update(house_rent_type=house_rent_type) if house_rent_type else None
        house_ojb.update(house_area=house_area) if house_area else None
        house_ojb.update(house_price=house_price) if house_price else None
        house_ojb.update(bedroom_number=bedroom_number) if bedroom_number else None
        house_ojb.update(bathroom_number=bathroom_number) if bathroom_number else None
        house_ojb.update(house_detail=house_detail) if house_detail else None
        # house_ojb.update(house_img=house_img.name) if house_img else None

        if house_img:
            save_path = '../../static/{}/'.format(house_img.name)
            print(save_path, 123)
            with open(save_path, 'wb') as f:
                for content in house_img.chunks():
                    print(content, 123)
                    f.write(content)

        return Response({'info': '修改成功'})

    def delete(self, request):
        HouseInfoModel.objects.filter(house_id=1).delete()
        return Response({'info': '删除成功'})
