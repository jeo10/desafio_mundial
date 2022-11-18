from rest_framework.viewsets import ViewSet
from django.views.generic import TemplateView
from apps.mundial_predict.serializer import SeleccionSerializer, PartidoSerializer, PrediccionSerializer
from apps.mundial_predict.models import Seleccion, Partido, Prediccion
from rest_framework.response import Response
from rest_framework import status


class MundialView(TemplateView):
    template_name = 'index.html'


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

    def get_queryset(self, pk=None):
        if pk is None:
            return self.model.objects.all()
        else:
            return self.model.objects.filter(fase_desc=pk)

    def list(self, request):
        queryset = self.get_queryset()
        data = self.serializer_class(queryset, many=True).data
        return Response(data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset(pk)
        data = self.serializer_class(queryset, many=True).data
        return Response(data, status=status.HTTP_200_OK)


class PrediccionViewSet(ViewSet):
    serializer_class = PrediccionSerializer
    model = Prediccion

    def create(self, request):
        serializer = self.serializer_class(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'prediccion creada correctamente'}, status=status.HTTP_200_OK)
        return Response({'error': 'prediccion no creada'}, status=status.HTTP_400_BAD_REQUEST)
