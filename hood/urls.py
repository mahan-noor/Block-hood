from django.conf.urls import path,re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('',views.index,name='index'),
    re_path(r'^neighborhood/(\d+)',views.my_area,name ='hood'),
 
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


