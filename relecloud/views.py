from django.shortcuts import render
import os
from django.conf import settings


# Create your views here.
def index(request):
    return render(request, 'index.html')

# Create your views here.
def about(request):
    return render(request, 'about.html')

def image_gallery(request):
    media_root = os.path.join(os.getcwd(), 'media')
    images = [img for img in os.listdir(media_root) if img.endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    print(images)
    return render(request, 'gallery.html', {'images': images, 'MEDIA_URL': settings.MEDIA_URL,  # Asegúrate de pasar MEDIA_URL
})