from main.views import GetUsersView, DetalleUsuario
from django.urls import path

urlpatterns = [
    path('', GetUsersView.as_view() ),
    path('<int:id>', DetalleUsuario )
    ]

