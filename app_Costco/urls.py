from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_costco, name='inicio_costco'),
    path('usuarios/agregar/', views.agregar_usuario, name='agregar_usuario'),
    path('usuarios/', views.ver_usuario, name='ver_usuario'),
    path('usuarios/actualizar/<int:usuario_id>/', views.actualizar_usuario, name='actualizar_usuario'),
    path('usuarios/realizar_actualizacion/<int:usuario_id>/', views.realizar_actualizacion_usuario, name='realizar_actualizacion_usuario'),
    path('usuarios/borrar/<int:usuario_id>/', views.borrar_usuario, name='borrar_usuario'),
    # --- PRODUCTO ---
path('productos/agregar/', views.agregar_producto, name='agregar_producto'),
path('productos/', views.ver_producto, name='ver_producto'),
path('productos/actualizar/<int:producto_id>/', views.actualizar_producto, name='actualizar_producto'),
path('productos/realizar_actualizacion/<int:producto_id>/', views.realizar_actualizacion_producto, name='realizar_actualizacion_producto'),
path('productos/borrar/<int:producto_id>/', views.borrar_producto, name='borrar_producto'),
# --- PEDIDO ---
path('pedidos/agregar/', views.agregar_pedido, name='agregar_pedido'),
path('pedidos/', views.ver_pedido, name='ver_pedido'),
path('pedidos/actualizar/<int:pedido_id>/', views.actualizar_pedido, name='actualizar_pedido'),
path('pedidos/realizar_actualizacion/<int:pedido_id>/', views.realizar_actualizacion_pedido, name='realizar_actualizacion_pedido'),
path('pedidos/borrar/<int:pedido_id>/', views.borrar_pedido, name='borrar_pedido'),
# Categorías
    path('categoria/agregar/', views.agregar_categoria, name='agregar_categoria'),
    path('categoria/ver/', views.ver_categoria, name='ver_categoria'),
    path('categoria/actualizar/<int:id>/', views.actualizar_categoria, name='actualizar_categoria'),
    path('categoria/actualizar/guardar/<int:id>/', views.realizar_actualizacion_categoria, name='realizar_actualizacion_categoria'),
    path('categoria/borrar/<int:id>/', views.borrar_categoria, name='borrar_categoria'),

# Proveedores
    path('proveedor/agregar/', views.agregar_proveedor, name='agregar_proveedor'),
    path('proveedor/ver/', views.ver_proveedor, name='ver_proveedor'),
    path('proveedor/actualizar/<int:id>/', views.actualizar_proveedor, name='actualizar_proveedor'),
    path('proveedor/actualizar/guardar/<int:id>/', views.realizar_actualizacion_proveedor, name='realizar_actualizacion_proveedor'),
    path('proveedor/borrar/<int:id>/', views.borrar_proveedor, name='borrar_proveedor'),

# Empleados
    path('empleado/agregar/', views.agregar_empleado, name='agregar_empleado'),
    path('empleado/ver/', views.ver_empleado, name='ver_empleado'),
    path('empleado/actualizar/<int:id>/', views.actualizar_empleado, name='actualizar_empleado'),
    path('empleado/actualizar/guardar/<int:id>/', views.realizar_actualizacion_empleado, name='realizar_actualizacion_empleado'),
    path('empleado/borrar/<int:id>/', views.borrar_empleado, name='borrar_empleado'),

# Ventas
    path('ventas/agregar/', views.agregar_ventas, name='agregar_ventas'),
    path('ventas/ver/', views.ver_ventas, name='ver_ventas'),
    path('ventas/actualizar/<int:id>/', views.actualizar_ventas, name='actualizar_ventas'),
    path('ventas/actualizar/guardar/<int:id>/', views.realizar_actualizacion_ventas, name='realizar_actualizacion_ventas'),
    path('ventas/borrar/<int:id>/', views.borrar_ventas, name='borrar_ventas'),
]