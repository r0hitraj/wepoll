from django.urls import path
from .import views
from django.contrib.auth import views as auth_views


urlpatterns=[

    path('',views.index, name='index'),   #route of index page
    path('join/',views.join, name='join'),   #route of join page
    path('addq',views.addq, name='addq'),   #route of addq page
    path('add',views.add, name='add'),   #route of add page
    path('stats/',views.stats,name='stats'), #route of the stats page
    path('submit',views.submit,name='submit'), #route of the submit page
    path('manage',views.manage,name='manage'), #route of the manage page
    path('create',views.create ,name='create'), #route of the create page
    path('logout',views.logout ,name='logout'),
     path('delt',views.delt,name='delt'), #route of the matches page

]