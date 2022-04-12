import datetime
import json
import time

from dateutil import rrule

from rest_framework.response import Response
from rest_framework.views import APIView

from polls.models import OrderInfoModel, UserModel, HouseInfoModel
from django.db.models import Q, F


class InsertHouseDetail(APIView):
    def post(self, requests):
        user_id = requests.POST.get('user_id')  # 用户ID
        house_city = requests.POST.get('house_city')  # 房屋所在城市
        house_location = requests.POST.get('house_location')  # 房屋所在地理位置
        house_number = requests.POST.get('house_number')  # 房屋门牌号
        house_rent_type = requests.POST.get('house_rent_type')  # 房屋租赁类型
        house_area = requests.POST.get('house_area')  # 房屋面积
        house_price = requests.POST.get('house_price')  # 租赁价格
        bedroom_number = requests.POST.get('bedroom_number')  # 卧室数量
        bathroom_number = requests.POST.get('bathroom_number')  # 洗手间数量
        house_detail = requests.POST.get('house_detail')  # 房屋明细
        house_img = requests.FILES.get('house_img')  # 房屋图片
        house_img_detail_1 = requests.FILES.get('house_img_detail_1')  # 图片明细
        house_img_detail_2 = requests.FILES.get('house_img_detail_2')  # 图片明细
        house_img_detail_3 = requests.FILES.get('house_img_detail_3')  # 图片明细
        house_img_detail_4 = requests.FILES.get('house_img_detail_4')  # 图片明细
        house_img_detail_5 = requests.FILES.get('house_img_detail_5')  # 图片明细
        house_img_detail_6 = requests.FILES.get('house_img_detail_6')  # 图片明细

        img_str = ''
        for i in range(1, 6):
            if eval('house_img_detail_' + str(i)):
                print(eval('house_img_detail_' + str(i)).name, 123)
                img_str += eval('house_img_detail_' + str(i)).name + ','
                save_path = '/Users/loctek/PycharmProjects/rent_house/static/{}'.format(
                    eval('house_img_detail_' + str(i)).name)
                with open(save_path, 'wb') as f:
                    for content in eval('house_img_detail_' + str(i)).chunks():
                        f.write(content)

        # print(house_img.name, 123)
        house_obj = HouseInfoModel(user_id=user_id, house_city=house_city, house_location=house_location,
                                   house_number=house_number, house_rent_type=house_rent_type, house_area=house_area,
                                   house_price=house_price, bedroom_number=bedroom_number,
                                   bathroom_number=bathroom_number, house_detail=house_detail,
                                   house_img=house_img.name, house_type=0, is_delete=1, date=datetime.datetime.now(),
                                   house_img_detail=img_str)
        if house_img:
            save_path = '/Users/loctek/PycharmProjects/rent_house/static/{}'.format(house_img.name)
            with open(save_path, 'wb') as f:
                for content in house_img.chunks():
                    f.write(content)
        house_obj.save()

        return Response({'info': '插入成功'})
