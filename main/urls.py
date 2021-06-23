
from .views import DeleteUserView, GetUsersView, DetalleUsuario, UpdateUserView,createUserView
from django.urls import path

app_name='main'

urlpatterns = [
    path('', GetUsersView.as_view(), name='list' ),
    path('<int:id>/', DetalleUsuario,  name ='detail' ),
    path('create/', createUserView.as_view(), name='create' ),
    path('update/<int:id>/', UpdateUserView.as_view(), name='update'),
    path('delete/<int:id>/', DeleteUserView, name='delete' )
  
    ]

