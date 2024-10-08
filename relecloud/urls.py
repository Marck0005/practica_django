from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('destinations', views.destinations, name='destinations'),
    path('cruises', views.cruises, name='cruises'),
    path('destination/<int:pk>', views.DestinationDetailView.as_view(), name= 'destination_detail'),
    path('destination/create', views.DestinationCreateView.as_view(), name= 'destination_form'),
    path('destination/<int:pk>/update', views.DestinationUpdateView.as_view(), name= 'destination_form'),
    path('destination/<int:pk>/delete', views.DestinationDeleteView.as_view(), name= 'destination_confirm_delete'),
    
]