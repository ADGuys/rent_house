from polls import models
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserModel
        # fields = ['name', 'phone_number']
        fields = '__all__'

# class HouseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.HouseInfoModel
#         fields = '__all__'
