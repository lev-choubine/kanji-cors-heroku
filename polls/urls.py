from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/<kanji_id>', views.kanji_request, name='kanji_request')
]
