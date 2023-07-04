from rest_framework import serializers
from .models import Lice,Film

class LiceSerializers(serializers.ModelSerializer):

    class Meta:
        model = Lice
        fields = "__all__"
       ## fields = ["ime", "prezime", "email"]

    def create(self, validated_data):
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)


"""class FilmSerializers(serializers.ModelSerializer):

    class Meta:
        model = Film
        fields = "__all__" """


