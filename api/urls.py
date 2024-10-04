from django.urls import path,include
from api import views
from rest_framework import routers

router=routers.DefaultRouter()

#the r is added to the left of the string to make it a raw string
router.register(r'products', views.ProductViewSet)

urlpatterns=[
    path('',include(router.urls))
]