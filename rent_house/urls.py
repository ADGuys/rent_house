"""rent_house URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from polls.views import list_user, list_house, list_order, list_order_detail, list_type_count
from django.views.static import serve

from rent_house import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/user/', list_user.ListUser.as_view()),
    path('list/house/', list_house.ListHouse.as_view()),
    path('list/order/', list_order.ListOrder.as_view()),
    path('list/order/detail', list_order_detail.ListOrderDetail.as_view()),
    path('list/type/count', list_type_count.ListTypeCount.as_view()),
]
