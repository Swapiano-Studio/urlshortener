from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import URLShortenerViewSet, redirect_to_original, get_short_url

# Create a router and register the viewset with it
router = DefaultRouter()
router.register(r'urls', URLShortenerViewSet, basename='urlshortener')

# Define the URL patterns
urlpatterns = [
    path('', include(router.urls)),  # Include the router's URLs
    path('r/<str:short_url>/', redirect_to_original, name='redirect_to_original'),
    path('stats/<str:short_url>/', get_short_url, name='get_short_url'),
]