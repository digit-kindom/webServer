"""
URL configuration for newdjangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path

from device import views

urlpatterns = [
    path('',views.index),    #网页直接访问，helloworld
    path('debug/binary', views.id_create),

    path('debug/binary', views.id_list_time),  # 依据时间对设备进行数据查询
    path('debug/binary', views.id_history_state),  # 数据设备历史状态查询
    path('debug/binary', views.information_add),  # 添加数据（多次与一次）
    path('debug/binary', views.id_delete),  # 数据的删除
]