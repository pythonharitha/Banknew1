from django.urls import path

from  .import views

urlpatterns = [

    path('', views.index,name='index'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('home/',views.home,name='home'),
    path('new/',views.new,name='new'),
    path('member/add/',views.create_view,name='list'),

    ]
