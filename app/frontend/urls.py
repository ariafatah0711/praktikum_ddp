from django.urls import path

from .views import home, contact, about

app_name = 'frontend'

urlpatterns = [
    path('', home, name='index'),
    path('home/', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact')
]
