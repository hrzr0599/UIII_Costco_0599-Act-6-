from django.contrib import admin
from .models import Usuario, Producto, Pedido
from .models import Empleado, Ventas, Categoria, Proveedor

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id','nombre_usuario','email','nombre','apellido','fecha_registro')
    search_fields = ('nombre_usuario','email','nombre','apellido')

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','precio','stock','categoria','fecha_creacion')
    search_fields = ('nombre','codigo_barras')

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'fecha_pedido', 'estado_pedido', 'total_pedido')
    search_fields = ('usuario__nombre_usuario', 'numero_seguimiento')
    list_filter = ('estado_pedido', 'fecha_pedido')

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'salario', 'fecha_contratacion', 'fecha_registro')
    search_fields = ('nombre', 'apellido')
    list_filter = ('fecha_contratacion', 'fecha_registro')

@admin.register(Ventas)
class VentasAdmin(admin.ModelAdmin):
    list_display = ('id', 'producto', 'usuario', 'vendedor', 'total', 'metodo_pago', 'fecha_venta')
    search_fields = ('producto__nombre', 'usuario__nombre', 'vendedor__nombre')
    list_filter = ('metodo_pago', 'fecha_venta')

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'email', 'telefono')
    search_fields = ('nombre', 'email')