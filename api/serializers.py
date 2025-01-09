# mailer/serializers.py

from rest_framework import serializers


class EmailSerializer(serializers.Serializer):
    address = serializers.EmailField()
    subject = serializers.CharField(max_length=255)
    message = serializers.CharField()

