## ✅ 7. Aplicaciones preinstaladas en Django y su utilidad

Django incluye varias aplicaciones preinstaladas que sirven como soporte para el desarrollo del proyecto. Estas aplicaciones están en django.contrib y proporcionan funcionalidades esenciales sin necesidad de crearlas desde cero.

Las principales aplicaciones utilizadas son:

### ✔ django.contrib.admin

Proporciona el panel de administración de Django, que permite gestionar los modelos de la aplicación sin necesidad de crear vistas manuales.

Función principal:

Crear, editar y eliminar registros desde una interfaz segura y automática.

Uso en este proyecto:
Se registraron los modelos para permitir administrar datos desde el panel.

```bash
from django.contrib import admin
from .models import Producto, Pedido, Cliente, PerfilCliente

admin.site.register(Producto)
admin.site.register(Pedido)
admin.site.register(Cliente)
admin.site.register(PerfilCliente)
```
### ✔ django.contrib.auth

Sistema de autenticación de Django.

Función principal:

Manejo de usuarios, permisos y autenticación.

Utilidad en el proyecto:

Permite acceder al admin con un superusuario.

Controla permisos para modificar modelos.

### ✔ django.contrib.sessions

Maneja las sesiones de usuarios.

Función principal:

Guardar datos de usuario entre solicitudes (por ejemplo, mantener una sesión iniciada).

Utilidad en el proyecto:

Permite que el inicio de sesión del admin se mantenga mientras el navegador está activo.

### ✔ django.contrib.messages

Módulo para enviar mensajes temporales.

Función principal:

Mostrar alertas como "producto creado", "producto eliminado", etc.

Uso en este proyecto:
Las vistas de CRUD utilizan messages.success() y messages.warning() para notificaciones.

### ✔ django.contrib.staticfiles

Gestiona archivos estáticos como CSS, JS e imágenes.

Función principal:

Permitir que los templates carguen Bootstrap, estilos, scripts, etc.