from django.urls import path , include
from rest_framework import routers
from .views import *


router = routers.DefaultRouter()
router.register(r'contacts', ContactsViewSet )

urlpatterns = [
     path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]


urlpatterns += router.urls


