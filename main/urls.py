from main.views import GetUsersView
from django.urls import path

urlpatterns = [
    path('', GetUsersView.as_view() )
    ]

