from django.urls import path
from Api1 import views
from Api1.views import ProductoViewSet

from rest_framework.routers import DefaultRouter



router= DefaultRouter()
router.register(r'ListaPrecio',ProductoViewSet)
urlpatterns=router.urls

urlpatterns += [

]
