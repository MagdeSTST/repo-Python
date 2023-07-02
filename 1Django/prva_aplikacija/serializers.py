from rest_framework import serializers
from .models import Lice

class LiceSerializers(serializers.ModelSerializer):

    class Meta:
        model = Lice
        fields = "__all__"