from django.urls import path
from . import views
urlpatterns = [
    path('',views.register,name='register'),
    path('userlogin/',views.userlogin,name='userlogin'),
    path('userlogout/',views.userlogout,name='userlogout'),
    path('setting/',views.setting,name='setting'),
    path('homepage/',views.homepage,name='homepage')

]