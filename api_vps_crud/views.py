from drf_yasg import openapi
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from .models import Vps
from .serializers import VpsSerializers
from .utils import serializer_data, create_status_description


class VpsViewSet(viewsets.ModelViewSet):
    queryset = Vps.objects.all()
    serializer_class = VpsSerializers
    http_method_names = ['get', 'post', 'patch', "delete"]
    status_desc = create_status_description(Vps.STATUS_VPS)

    @swagger_auto_schema(query_serializer=VpsSerializers,
                         operation_summary="Получение списка VPS-серверов по заданным фильтрам.",
                         operation_description=status_desc)
    @action(methods=["get"], detail=False, url_path="filter")
    def filter_vps(self, request):
        """Поиск VPS серверов по заданным фильтрам."""
        data_req = serializer_data(VpsSerializers, request.GET, partial=True)
        vps_list = Vps.objects.filter(**data_req)

        return Response(VpsSerializers(vps_list, many=True).data)

    @swagger_auto_schema(operation_summary="Удаление VPS-сервера.",
                         responses={"204": openapi.Response(
                             description="VPS-сервер удален.",
                             examples={"application/json": {"detail": "vps_deleted"}}
                         )})
    def destroy(self, request, *args, **kwargs):
        """Удаляет VPS-сервер."""
        super().destroy(request, *args, **kwargs)
        return Response({"detail": "vps_deleted"})

    @swagger_auto_schema(operation_summary="Получение списка всех VPS-серверов.",
                         operation_description=status_desc)
    def list(self, request, *args, **kwargs):
        """Возвращает весь список VPS-серверов."""
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Получение VPS-сервера по uid.",
                         operation_description=status_desc)
    def retrieve(self, request, *args, **kwargs):
        """Возвращает VPS-сервер по uid."""
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Создание нового VPS-сервера.",
                         operation_description=status_desc)
    def create(self, request, *args, **kwargs):
        """Создает VPS-сервер."""
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Изменение данных VPS-сервера.",
                         operation_description=status_desc)
    def partial_update(self, request, *args, **kwargs):
        """Изменяет данные VPS-сервера."""
        return super().partial_update(request, *args, **kwargs)
