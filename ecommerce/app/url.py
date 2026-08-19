from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.register,name='register'),
    path('userlogin/',views.userlogin,name='userlogin'),
    path('userlogout/',views.userlogout,name='userlogout'),
    path('setting/',views.setting,name='setting'),
    path('homepage/',views.homepage,name='homepage'),
    path('fashion/',views.fashion,name='fashion'),
    path('electronic/',views.electronic,name='electronic'),
    path('footwear/',views.footwear,name='footware'),
    path('homerelated/',views.homerelated,name='homerelated'),









    path('test-email/', views.test_email, name='test_email'),

    # password reset
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='password_reset.html'),name='password_reset'),

    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),

    path('password-reset-conform/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),

    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete')


]