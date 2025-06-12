from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, redirect
from .serializers import URLShortenerSerializer
from .models import URLShortener
import random, string

# Create your views here.
class URLShortenerViewSet(viewsets.ModelViewSet):
    queryset = URLShortener.objects.all()
    serializer_class = URLShortenerSerializer

    def create(self, request, *args, **kwargs):
        original_url = request.data.get('original_url')
        if not original_url:
            return Response({"error": "Original URL is required."}, status=status.HTTP_400_BAD_REQUEST)

        short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        url_instance = URLShortener(original_url=original_url, short_url=short_url)
        url_instance.save()

        serializer = self.get_serializer(url_instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
@api_view(['GET'])
def redirect_to_original(request, short_url):
    url_instance = get_object_or_404(URLShortener, short_url=short_url)
    url_instance.clicks += 1
    url_instance.save()
    return redirect(url_instance.original_url)

@api_view(['GET'])
def get_short_url(request, short_url):
    url_instance = get_object_or_404(URLShortener, short_url=short_url)
    serializer = URLShortenerSerializer(url_instance)
    return Response(serializer.data, status=status.HTTP_200_OK)