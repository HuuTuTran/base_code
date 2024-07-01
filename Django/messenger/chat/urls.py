"""
URL configuration for messenger project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from chat import views
urlpatterns = [
    path("messengers/<int:group_id>", views.chat_view , name = "chat_view"),
    path("", views.chat_view , name = "chat_view"),
    path("submit_login",views.login,name = "login"),
    path("login",views.login_view,name="login_view"),
    path("sign_out",views.sign_out,name="sign_out"),
    path("send_mess/<int:group_id>",views.send_mess,name="send_mess"),
    path("refresh/<int:group_id>",views.refresh_data,name="rf_data")
    # path("friends_mess/<int:friend_id>",views.get_group_id_by_friend_id,name= "get_group_id_by_friend_id")
]
