from django.urls import path
from app2.views import *
app_name='haiii'
urlpatterns=[
    path('specific2/',specific2,name='specific2'),
]