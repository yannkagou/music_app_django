from rest_framework import serializers

from core.serializers import UserSerializer

from .models import Subscriber


class SubscriberSerializer(serializers.ModelSerializer):
    # user_id = serializers.IntegerField(read_only=True)
    user = UserSerializer(read_only=True)
    class Meta:
        model = Subscriber
        fields = ['id', 'user', 'birth_date']
