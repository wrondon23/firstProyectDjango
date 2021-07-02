
 
from .views import GetaddressesView,CreateShippingAddressViews, UpdateShippingAddressViews,DeleteShippinAddressView
from django.urls import path

app_name='shipping_addresses'

urlpatterns = [
    path('<int:id>/', GetaddressesView, name='detail' ),
    path('create/<int:user_id>/', CreateShippingAddressViews.as_view(), name='create' ),
    path('update/<int:id>/', UpdateShippingAddressViews.as_view(), name='update' ),
    path('delete/<int:id>/', DeleteShippinAddressView, name='delete' )
    ]
