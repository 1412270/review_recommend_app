from rest_framework.serializers import ModelSerializer
from .models import Movies, User


class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movies
        fields = "__all__"


class UserSerializer(ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)

        return user

    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extract_kwargs = {
            'password': {'write_only': 'true'}
        }
