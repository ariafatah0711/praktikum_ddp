from django.urls import path

from .views import home, about, gallery, contact

app_name = 'frontend'

urlpatterns = [
    path('', home, name='index'),
    path('home/', home, name='home'),
    path('about/', about, name='about'),
    path('gallery/', gallery, name='gallery'),
    path('contact/', contact, name='contact')
]
