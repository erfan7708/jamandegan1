from django.urls import path

from . import views

urlpatterns = [
    path('', views.navbar , name='index'),
    path('login' ,views.log_in , name='log-in'),
    path('signup_view', views.signup_view, name='sign-up_view'),
    path('logout',views.log_out , name='log-out'),
    path('contact_us',views.contact,name='contact-us'),
    #path('user_profile',views.user_profile,name='user_profile')
]