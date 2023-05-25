from rest_framework import serializers
from movies_api.models import Movies

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = '__all__'