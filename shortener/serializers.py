from rest_framework import serializers
from .models import URLShortener
from django.conf import settings
# Ensure that the URLShortener model is imported correctly

class URLShortenerSerializer(serializers.ModelSerializer):
    class Meta:
        model = URLShortener

        fields = ['id', 'original_url', 'short_url', 'created_at', 'clicks']
        read_only_fields = ['id', 'short_url', 'created_at', 'clicks']  # Make these fields read-only

