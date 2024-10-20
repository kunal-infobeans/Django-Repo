from django.urls import path
from first_app import views
from django.conf.urls import include

app_name = 'first_app'

urlpatterns = [
    # path('relative/',views.relative,name='relative'),
    path('user_login/',views.user_login,name='user_login'),
    path('register/',views.register,name='register'),
    path('',views.index,name='index'),
]