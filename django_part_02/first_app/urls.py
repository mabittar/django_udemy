from django.urls import path

from first_app import views  # type: ignore

app_name = 'first'
urlpatterns = [
    path('', views.index, name='index'),
]

