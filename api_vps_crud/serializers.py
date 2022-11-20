from rest_framework import serializers

from .models import Vps


class VpsSerializers(serializers.ModelSerializer):

    class Meta:
        model = Vps
        fields = "__all__"
