from django.urls import path
from . import views

urlpatterns = [
    path('productos/', views.listar_productos, name='listar_productos'),
    path('productosView/', views.productos_view, name="productos_view"),
    path('productos/modificar/<int:id>/', views.modificar_producto, name="modificar_producto"),
    path('productos/eliminar/<int:id>/', views.eliminar_producto, name="eliminar_producto"),
]
