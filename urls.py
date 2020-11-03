from django.urls import path
from . import views

urlpatterns = (
    path('', views.dashboard, name="dashboard"),
    path('login/', views.l_login, name="login"),
    path('logout/', views.logoutt, name='logout'),
    path('register/', views.reg_before, name='reg_before'),
    path('member/', views.member_page, name="member"),
    path('member/member_form', views.member_form, name="member_form"),
    path('member_user/', views.member_user, name="member_user"),
    path('member_register/', views.member_register, name='mem_reg'),
    path('member_list/', views.member_list, name='member_list'),
    path('member_details/<str:id>',views.member_details,name='member_details'),
    path('member_settings/<str:id>',views.member_settings,name='member_settings'),
    path('investor', views.investor_page, name="investor"),
    path('investor_user/', views.investor_user, name="investor_user"),
    path('investor/investor_form', views.investor_form, name="investor_form"),
    path('investor_register/', views.investor_register, name='inv_reg'),
    path('investor_list/', views.investor_list, name='investor_list'),
    path('investor_details/<str:id>',views.investor_details,name='investor_details'),
    path('investor_settings/<str:id>',views.investor_settings,name='investor_settings'),
    path('startup/', views.startup_page, name="startup"),
    path('startup_user/', views.startup_user, name="startup_user"),
    path('startup/startup_form', views.startup_form, name="startup_form"),
    path('startup_register/', views.startup_register, name='sta_reg'),
    path('startup_list/', views.startup_list, name='startup_list'),
    path('startup_details/<str:id>',views.startup_details,name='startup_details'),
    path('startup_settings/<str:id>',views.startup_settings,name='startup_settings'),
)