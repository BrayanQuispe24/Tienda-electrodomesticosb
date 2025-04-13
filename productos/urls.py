# urls.py
from django.urls import path
from .views import crear_producto, actualizar_producto, obtener_productos, obtener_producto,obtener_detalles_producto

urlpatterns = [
    path('crear/', crear_producto),
    path('actualizar/', actualizar_producto),
    path('producto', obtener_productos),
    path('producto/<int:id>', obtener_producto),
    path('producto_with_information',obtener_detalles_producto)
]
