from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Usuario

def inicio_costco(request):
    return render(request, 'inicio.html')

# Mostrar formulario para agregar usuario y procesar POST
def agregar_usuario(request):
    if request.method == 'POST':
        nombre_usuario = request.POST.get('nombre_usuario', '').strip()
        email = request.POST.get('email', '').strip()
        nombre = request.POST.get('nombre', '').strip()
        apellido = request.POST.get('apellido', '').strip()
        direccion = request.POST.get('direccion', '').strip()
        telefono = request.POST.get('telefono', '').strip()

        usuario = Usuario(
            nombre_usuario=nombre_usuario,
            email=email,
            nombre=nombre,
            apellido=apellido,
            direccion=direccion,
            telefono=telefono
        )
        usuario.save()
        return redirect('ver_usuario')
    # GET -> mostrar formulario
    return render(request, 'usuario/agregar_usuario.html')

# Ver lista de usuarios
def ver_usuario(request):
    usuarios = Usuario.objects.all().order_by('-fecha_registro')
    return render(request, 'usuario/ver_usuario.html', {'usuarios': usuarios})

# Mostrar formulario de actualización (carga datos)
def actualizar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    return render(request, 'usuario/actualizar_usuario.html', {'usuario': usuario})

# Procesar actualización (POST)
def realizar_actualizacion_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    if request.method == 'POST':
        usuario.nombre_usuario = request.POST.get('nombre_usuario', usuario.nombre_usuario).strip()
        usuario.email = request.POST.get('email', usuario.email).strip()
        usuario.nombre = request.POST.get('nombre', usuario.nombre).strip()
        usuario.apellido = request.POST.get('apellido', usuario.apellido).strip()
        usuario.direccion = request.POST.get('direccion', usuario.direccion).strip()
        usuario.telefono = request.POST.get('telefono', usuario.telefono).strip()
        usuario.save()
        return redirect('ver_usuario')
    return redirect('actualizar_usuario', usuario_id=usuario_id)

# Confirmar y borrar usuario
def borrar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('ver_usuario')
    return render(request, 'usuario/borrar_usuario.html', {'usuario': usuario})



from .models import Producto

# Agregar producto
def agregar_producto(request):
    proveedores = Proveedor.objects.all()
    categorias = Categoria.objects.all()

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        stock = request.POST.get('stock')
        codigo_barras = request.POST.get('codigo_barras')
        imagen_url = request.POST.get('imagen_url')
        proveedor_id = request.POST.get('proveedor')
        categoria_id = request.POST.get('categoria')

        proveedor = Proveedor.objects.get(id=proveedor_id)
        categoria = Categoria.objects.get(id=categoria_id)

        Producto.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            stock=stock,
            codigo_barras=codigo_barras,
            imagen_url=imagen_url,
            proveedor=proveedor,
            categoria=categoria
        )
        return redirect('ver_producto')

    return render(request, 'producto/agregar_producto.html', {'proveedores': proveedores, 'categorias': categorias})



# Ver productos
def ver_producto(request):
    productos = Producto.objects.all().order_by('-fecha_creacion')
    return render(request, 'producto/ver_producto.html', {'productos': productos})


# Mostrar formulario de actualización
def actualizar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    proveedores = Proveedor.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'producto/actualizar_producto.html', {
        'producto': producto,
        'proveedores': proveedores,
        'categorias': categorias
    })


# Realizar actualización
def realizar_actualizacion_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.nombre = request.POST.get('nombre')
        producto.descripcion = request.POST.get('descripcion')
        producto.precio = request.POST.get('precio')
        producto.stock = request.POST.get('stock')
        # actualizar relaciones por id
        proveedor_id = request.POST.get('proveedor')
        categoria_id = request.POST.get('categoria')
        if proveedor_id:
            producto.proveedor_id = proveedor_id
        else:
            producto.proveedor = None
        if categoria_id:
            producto.categoria_id = categoria_id
        else:
            producto.categoria = None
        producto.codigo_barras = request.POST.get('codigo_barras')
        producto.imagen_url = request.POST.get('imagen_url')
        producto.save()
        return redirect('ver_producto')
    return redirect('actualizar_producto', producto_id=producto_id)


# Borrar producto
def borrar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('ver_producto')
    return render(request, 'producto/borrar_producto.html', {'producto': producto})


from .models import Usuario, Producto, Pedido
from django.shortcuts import render, redirect, get_object_or_404

# -----------------------------
# CRUD PEDIDO
# -----------------------------

# AGREGAR PEDIDO
def agregar_pedido(request):
    usuarios = Usuario.objects.all()
    productos = Producto.objects.all()

    if request.method == 'POST':
        usuario_id = request.POST.get('usuario')
        direccion_envio = request.POST.get('direccion_envio')
        total_pedido = request.POST.get('total_pedido')
        metodo_pago = request.POST.get('metodo_pago')
        estado_pedido = request.POST.get('estado_pedido')
        productos_ids = request.POST.getlist('productos')

        usuario = Usuario.objects.get(id=usuario_id)
        pedido = Pedido.objects.create(
            usuario=usuario,
            direccion_envio=direccion_envio,
            total_pedido=total_pedido,
            metodo_pago=metodo_pago,
            estado_pedido=estado_pedido
        )
        pedido.productos.set(productos_ids)
        return redirect('ver_pedido')

    return render(request, 'pedido/agregar_pedido.html', {
        'usuarios': usuarios,
        'productos': productos
    })


# VER PEDIDOS
def ver_pedido(request):
    pedidos = Pedido.objects.all().order_by('-fecha_pedido')
    return render(request, 'pedido/ver_pedido.html', {'pedidos': pedidos})


# ACTUALIZAR PEDIDO (mostrar formulario)
def actualizar_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    usuarios = Usuario.objects.all()
    productos = Producto.objects.all()
    return render(request, 'pedido/actualizar_pedido.html', {
        'pedido': pedido,
        'usuarios': usuarios,
        'productos': productos
    })


# REALIZAR ACTUALIZACIÓN DE PEDIDO
def realizar_actualizacion_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    if request.method == 'POST':
        pedido.usuario_id = request.POST.get('usuario')
        pedido.direccion_envio = request.POST.get('direccion_envio')
        pedido.total_pedido = request.POST.get('total_pedido')
        pedido.metodo_pago = request.POST.get('metodo_pago')
        pedido.estado_pedido = request.POST.get('estado_pedido')
        pedido.save()

        productos_ids = request.POST.getlist('productos')
        pedido.productos.set(productos_ids)
        return redirect('ver_pedido')
    return redirect('actualizar_pedido', pedido_id=pedido_id)


# BORRAR PEDIDO
def borrar_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    if request.method == 'POST':
        pedido.delete()
        return redirect('ver_pedido')
    return render(request, 'pedido/borrar_pedido.html', {'pedido': pedido})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Categoria, Proveedor

# ==============================
# CRUD PARA CATEGORÍA
# ==============================

def agregar_categoria(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        Categoria.objects.create(nombre=nombre)
        return redirect('ver_categoria')
    return render(request, 'categoria/agregar_categoria.html')


def ver_categoria(request):
    categorias = Categoria.objects.all()
    return render(request, 'categoria/ver_categoria.html', {'categorias': categorias})


def actualizar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    return render(request, 'categoria/actualizar_categoria.html', {'categoria': categoria})


def realizar_actualizacion_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    if request.method == 'POST':
        categoria.nombre = request.POST.get('nombre')
        categoria.save()
        return redirect('ver_categoria')
    return redirect('ver_categoria')


def borrar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    categoria.delete()
    return redirect('ver_categoria')


# ==============================
# CRUD PARA PROVEEDOR
# ==============================

def agregar_proveedor(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        nombre_contacto_principal = request.POST.get('nombre_contacto_principal')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email')
        direccion = request.POST.get('direccion')
        Proveedor.objects.create(
            nombre=nombre,
            nombre_contacto_principal=nombre_contacto_principal,
            telefono=telefono,
            email=email,
            direccion=direccion
        )
        return redirect('ver_proveedor')
    return render(request, 'proveedor/agregar_proveedor.html')


def ver_proveedor(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedor/ver_proveedor.html', {'proveedores': proveedores})


def actualizar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id=id)
    return render(request, 'proveedor/actualizar_proveedor.html', {'proveedor': proveedor})


def realizar_actualizacion_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id=id)
    if request.method == 'POST':
        proveedor.nombre = request.POST.get('nombre')
        proveedor.nombre_contacto_principal = request.POST.get('nombre_contacto_principal')
        proveedor.telefono = request.POST.get('telefono')
        proveedor.email = request.POST.get('email')
        proveedor.direccion = request.POST.get('direccion')
        proveedor.save()
        return redirect('ver_proveedor')
    return redirect('ver_proveedor')


def borrar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id=id)
    proveedor.delete()
    return redirect('ver_proveedor')


# ==============================
# CRUD PARA EMPLEADO
# ==============================

from .models import Empleado

def agregar_empleado(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        salario = request.POST.get('salario')
        fecha_contratacion = request.POST.get('fecha_contratacion')
        Empleado.objects.create(
            nombre=nombre,
            apellido=apellido,
            salario=salario,
            fecha_contratacion=fecha_contratacion
        )
        return redirect('ver_empleado')
    return render(request, 'empleado/agregar_empleado.html')


def ver_empleado(request):
    empleados = Empleado.objects.all().order_by('-fecha_registro')
    return render(request, 'empleado/ver_empleado.html', {'empleados': empleados})


def actualizar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    return render(request, 'empleado/actualizar_empleado.html', {'empleado': empleado})


def realizar_actualizacion_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    if request.method == 'POST':
        empleado.nombre = request.POST.get('nombre')
        empleado.apellido = request.POST.get('apellido')
        empleado.salario = request.POST.get('salario')
        empleado.fecha_contratacion = request.POST.get('fecha_contratacion')
        empleado.save()
        return redirect('ver_empleado')
    return redirect('ver_empleado')


def borrar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    if request.method == 'POST':
        empleado.delete()
        return redirect('ver_empleado')
    return render(request, 'empleado/borrar_empleado.html', {'empleado': empleado})


# ==============================
# CRUD PARA VENTAS
# ==============================

from .models import Ventas

def agregar_ventas(request):
    productos = Producto.objects.all()
    usuarios = Usuario.objects.all()
    empleados = Empleado.objects.all()

    if request.method == 'POST':
        producto_id = request.POST.get('producto')
        usuario_id = request.POST.get('usuario')
        vendedor_id = request.POST.get('vendedor')
        total = request.POST.get('total')
        metodo_pago = request.POST.get('metodo_pago')
        descuento = request.POST.get('descuento', 0)

        producto = Producto.objects.get(id=producto_id)
        usuario = Usuario.objects.get(id=usuario_id)
        vendedor = Empleado.objects.get(id=vendedor_id)

        Ventas.objects.create(
            producto=producto,
            usuario=usuario,
            vendedor=vendedor,
            total=total,
            metodo_pago=metodo_pago,
            descuento=descuento
        )
        return redirect('ver_ventas')

    return render(request, 'ventas/agregar_ventas.html', {
        'productos': productos,
        'usuarios': usuarios,
        'empleados': empleados
    })


def ver_ventas(request):
    ventas = Ventas.objects.all().order_by('-fecha_venta')
    return render(request, 'ventas/ver_ventas.html', {'ventas': ventas})


def actualizar_ventas(request, id):
    venta = get_object_or_404(Ventas, id=id)
    productos = Producto.objects.all()
    usuarios = Usuario.objects.all()
    empleados = Empleado.objects.all()
    return render(request, 'ventas/actualizar_ventas.html', {
        'venta': venta,
        'productos': productos,
        'usuarios': usuarios,
        'empleados': empleados
    })


def realizar_actualizacion_ventas(request, id):
    venta = get_object_or_404(Ventas, id=id)
    if request.method == 'POST':
        venta.producto_id = request.POST.get('producto')
        venta.usuario_id = request.POST.get('usuario')
        venta.vendedor_id = request.POST.get('vendedor')
        venta.total = request.POST.get('total')
        venta.metodo_pago = request.POST.get('metodo_pago')
        venta.descuento = request.POST.get('descuento', 0)
        venta.save()
        return redirect('ver_ventas')
    return redirect('ver_ventas')


def borrar_ventas(request, id):
    venta = get_object_or_404(Ventas, id=id)
    if request.method == 'POST':
        venta.delete()
        return redirect('ver_ventas')
    return render(request, 'ventas/borrar_ventas.html', {'venta': venta})
