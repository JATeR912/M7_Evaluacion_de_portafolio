## ✅ 3. Modelos con relaciones (1–1, 1–N, N–N)

Se implementaron modelos con diferentes tipos de relaciones:

### ✔ Relación Uno a Uno (1–1)
```bash
class PerfilCliente(models.Model):
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE)
```
### ✔ Relación Uno a Muchos (1–N)
```bash
class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
```
### ✔ Relación Muchos a Muchos (N–N)
```bash
class Pedido(models.Model):
    productos = models.ManyToManyField(Producto)
```

Estos modelos representan correctamente diferentes formas de interacción entre entidades.

## ✅ 4. Uso de migraciones en Django

Para crear y modificar el esquema de la base de datos se utilizaron las migraciones del framework:
```bash
python manage.py makemigrations
python manage.py migrate
```

Cada vez que se modificó un modelo, se generó una migración nueva, cumpliendo el flujo correcto de trabajo en Django.

## ✅ 5. Consultas ORM y SQL personalizadas

Se generaron datos de prueba y se realizaron consultas utilizando el ORM y SQL.

### ✔ Abrir la shell de Django
```bash
python manage.py shell
```
### ✔ Importar los modelos
```bash
from producto_app.models import *
```
### ✔ Ejemplos de consultas ORM
# Filtrar productos por precio
```bash
Producto.objects.filter(precio__gte=10000)
```
# Obtener pedidos de un cliente específico
```bash
Pedido.objects.filter(cliente__id=1)
```
# Pedidos dentro de un rango de fechas
```bash
from datetime import date
Pedido.objects.filter(fecha__range=[date(2025,1,1), date(2025,11,18)])
```
# Excluir productos sin stock
```bash
Producto.objects.exclude(cantidad=0)
```
# Productos en un pedido
```bash
pedido = Pedido.objects.get(id=1)
pedido.productos.all()
```
# Contar pedidos por cliente
```bash
from django.db.models import Count
Cliente.objects.annotate(total_pedidos=Count('pedido'))
```
### ✔ Consulta SQL personalizada
```bash
from django.db import connection
cursor = connection.cursor()
cursor.execute("SELECT nombre, precio FROM producto_app_producto WHERE cantidad > 0")
resultados = cursor.fetchall()
```
## ✅ 6. Aplicación web MVC con CRUD

Se implementó una aplicación web basada en Django que permite:

✔ Crear productos
✔ Listar productos
✔ Ver detalles
✔ Editar
✔ Eliminar

Esto cumple con las operaciones CRUD utilizando el patrón MVC/MTV de Django.

Las vistas implementadas son:

- lista_productos

- detalle_producto

- crear_producto

- editar_producto

- eliminar_producto