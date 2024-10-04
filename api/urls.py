from django.urls import path,include
from rest_framework import routers

from api.views import ProductViewSet

router=routers.DefaultRouter()

#the r is added to the left of the string to make it a raw string
router.register(r'products', ProductViewSet)

urlpatterns=[
    path('',include(router.urls))
]