import collections

from rest_framework import serializers


def serializer_data(serializer_class: serializers, serialize_data, partial=False) -> collections.OrderedDict:
    """Сериалиация, валидация данных.

    :params serializer_class: класс сериализации
    :params serialize_data: данные для сериализации
    :params partial: флаг отвечающий за частичную сериализацию

    :return сериализованные данные
    """
    serializer = serializer_class(data=serialize_data, partial=partial)
    serializer.is_valid(raise_exception=True)
    return serializer.validated_data


def create_status_description(status_list):
    statuses_text = '\n'.join(['- '.join(field) for field in status_list])
    return f"Описание статусов\n{statuses_text}"
