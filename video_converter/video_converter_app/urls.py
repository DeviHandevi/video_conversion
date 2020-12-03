from django.urls import path

from . import views

app_name = 'video_conversion_app'
urlpatterns = [
    path('', views.index, name='index'),
]
