from rest_framework import serializers
from .models import TranscribedText

class TranscribedTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = TranscribedText
        fields = ["link", "text"]