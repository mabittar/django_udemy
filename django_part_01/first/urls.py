from django.urls import path

from first import views  # type: ignore

app_name = 'first'
urlpatterns = [
    path('', views.index, name='index'),
    path('help', views.help, name='help')
]


