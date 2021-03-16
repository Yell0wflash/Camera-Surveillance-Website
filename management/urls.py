from django.urls import path,include
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('addlocation',views.addlocation,name='addlocation'),
    path('addcamera',views.addcamera,name='addcamera'),
    path('do_add',views.do_location,name='do_addlocation'),
    path('do_add1',views.do_camera,name='do_addcamera'),
    path('showlocation',views.showlocation,name='showlocation'),
    path('showcamera',views.showcamera,name='showcamera'),
    path('assigncamera',views.assigncamera,name='assigncamera'),

]