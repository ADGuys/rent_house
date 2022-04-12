# Create your views here.111
# 还需要关联添加一些房屋信息

from rest_framework.response import Response
from rest_framework.views import APIView

from polls.models import HouseInfoModel, UserModel, PageNumberPagination
from rent_house import settings


class ListTypeCount(APIView):  # 查看房屋

    def get(self, requests):
        house_obj = HouseInfoModel.objects.filter(is_delete=1)
        count_house_type = 0
        count_house_status = 0
        count_house = 0
        item_dict = {}
        city_list = []
        for item in house_obj:
            count_house += 1
            count_house_type += 1 if item.house_rent_type else 0
            count_house_status += 1 if item.house_type else 0
            if item.house_city not in city_list:
                city_list.append(item.house_city)
                item_dict.update({
                    item.house_city: 1
                })
            else:
                item_dict.update({
                    item.house_city: item_dict[item.house_city] + 1
                })

        item_dict.update({
            '不限': count_house,
            '合租': count_house_type,
            '整租': count_house - count_house_type,
            '已出租': count_house_status,
            '未出租': count_house - count_house_status
        })
        for city_name in settings.CITY_LIST:
            item_dict.update({
                city_name: item_dict.get(city_name, 0)
            })
        return Response({'info': item_dict})

        # return Response({'info': item_list, 'total_page': total_page})
