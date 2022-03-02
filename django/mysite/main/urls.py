from django.urls import path
from . import views

# una vez qe se haya indicado el path, se debe de agregar las url de la carpeta pricipal
urlpatterns = [
    path('<int:id>', views.index, name='index'),
    path('', views.home, name='home')
]