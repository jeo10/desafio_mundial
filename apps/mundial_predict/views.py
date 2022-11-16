from rest_framework.viewsets import ViewSet
from apps.mundial_predict.serializer import SeleccionSerializer, PartidoSerializer
from apps.mundial_predict.models import Seleccion, Partido
from rest_framework.response import Response
from rest_framework import status


class SeleccionViewSet(ViewSet):
    serializer_class = SeleccionSerializer
    model = Seleccion

    def get_queryset(self):
        return self.model.objects.all()

    def list(self, request):
        queryset = self.get_queryset()
        data = self.serializer_class(queryset, many=True).data
        return Response(data, status=status.HTTP_200_OK)


class PartidoViewSet(ViewSet):
    serializer_class = PartidoSerializer
    model = Partido

    def get_queryset(self):
        return self.model.objects.all()

    def list(self, request):
        queryset = self.get_queryset()
        data = self.serializer_class(queryset, many=True).data
        return Response(data, status=status.HTTP_200_OK)
