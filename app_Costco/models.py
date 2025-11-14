from django.db import models


class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.TextField()
    telefono = models.CharField(max_length=20, blank=True, null=True)
    class MembresiaChoices(models.TextChoices):
        GOLD = 'Gold', 'Gold'
        EXECUTIVE = 'Executive', 'Executive'

    membresia = models.CharField(max_length=20, choices=MembresiaChoices.choices, default=MembresiaChoices.GOLD)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre_usuario


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre


class Proveedor(models.Model):
    nombre = models.CharField(max_length=150)
    nombre_contacto_principal = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    direccion = models.TextField()

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    codigo_barras = models.CharField(max_length=50, unique=True, blank=True, null=True)
    imagen_url = models.URLField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    # Relaciones nuevas
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name='productos')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, related_name='productos')

    def __str__(self):
        return self.nombre


class Pedido(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='pedidos')
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    estado_pedido = models.CharField(max_length=50, default='Pendiente')
    direccion_envio = models.TextField()
    total_pedido = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    metodo_pago = models.CharField(max_length=50)
    fecha_entrega_estimada = models.DateField(blank=True, null=True)
    numero_seguimiento = models.CharField(max_length=100, blank=True, null=True)
    productos = models.ManyToManyField(Producto, related_name='pedidos')

    def __str__(self):
        return f"Pedido #{self.id} de {self.usuario.nombre_usuario}"


class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_contratacion = models.DateField()
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Ventas(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='ventas')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='ventas_realizadas')
    vendedor = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name='ventas')
    fecha_venta = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(max_length=50)
    descuento = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Venta #{self.id} - {self.producto.nombre}"
