## ✅ 2. Modelos sin relaciones

Se implementó el modelo Producto, el cual no posee relaciones con otras entidades:
```bash
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.PositiveIntegerField(default=0)
    descripcion = models.TextField(default='Sin descripción')

    def __str__(self):
        return self.nombre
```

Este modelo representa una tabla independiente en la base de datos.