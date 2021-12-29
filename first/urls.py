# from django.urls import path
# from first import views
#
# urlpatterns=[path('',views.home)]


from .import views
from django.urls import path

urlpatterns=[
    path('',views.home,name='home'),
    path('pd',views.PersonalDetails,name='PersonalDetails'),
    path('add',views.add),
    path('showDetails',views.showDetails),
]

