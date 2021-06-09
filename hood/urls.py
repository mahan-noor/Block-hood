from django.urls import path,re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('',views.index,name='index'),
    re_path('neighborhood/(\d+)',views.my_area,name ='hood'),
    re_path('neighborhood/(\d+)',views.my_area,name ='hood'),
    re_path('neighborhood/(\d+)/join/',views.join,name ='join'),
    re_path('user/(?P<username>\w+)', views.profile, name='profile'),
    path('new/business', views.new_business, name='new-business')
 
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


