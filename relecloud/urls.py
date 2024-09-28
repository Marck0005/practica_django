from django.urls import path
from .views import image_gallery
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('gallery/', image_gallery, name='image_gallery'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
