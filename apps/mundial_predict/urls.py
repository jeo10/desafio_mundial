from django.urls import path
from rest_framework import routers
from apps.mundial_predict.views import *


router = routers.SimpleRouter()
router.register(r'seleccion', SeleccionViewSet, basename='seleccion')
router.register(r'partido', PartidoViewSet, basename='partido')
router.register(r'prediccion', PrediccionViewSet, basename='prediccion')
urlpatterns = [
    path('', MundialView.as_view(), name='home')
]
urlpatterns += router.urls
