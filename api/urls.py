from django.urls import path
from . import views


urlpatterns = [
    path('clientes', views.listar_clientes),
    path('usuarios', views.ClientesView.as_view()),
    path('usuario/<int:pk>', views.ClienteDetailView.as_view())
]


