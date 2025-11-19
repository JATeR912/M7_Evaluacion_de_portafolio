# 📁 Proyecto Django – Integración con Bases de Datos

Este proyecto demuestra la integración de Django con bases de datos, la implementación de modelos con y sin relaciones, migraciones, consultas ORM/SQL, una aplicación web MVC/CRUD y el uso de aplicaciones preinstaladas.

El proyecto está organizado en carpetas por cada requerimiento funcional del curso.

## Estructura de Carpetas y Contenidos
## 1️⃣ caracteristicas_django_db_1

Requisito 1 – Características fundamentales de Django con bases de datos

Explicación de cómo Django se conecta con diferentes motores de base de datos: SQLite, MySQL y PostgreSQL.

Configuración del archivo settings.py para cada base de datos.

Instalación de los conectores necesarios:

- sqlite3 (por defecto)

- mysqlclient o PyMySQL para MySQL

- psycopg2 para PostgreSQL

- Descripción del manejo de conexiones y operaciones mediante el ORM.

Archivos relevantes:

- README.md (documentación detallada de configuraciones y conectores)

## 2️⃣ modelo_no_relacionado_2

Requisito 2 – Modelos sin relaciones

Implementación de modelos simples de Django sin relaciones entre ellos.

Ejemplo: Modelo Producto con campos básicos (nombre, precio, cantidad, descripcion).

Cada modelo representa una tabla independiente en la base de datos.

Archivos relevantes:

- models.py (con el modelo Producto)

- README.md (documentación sobre el modelo y su propósito)

## 3️⃣ modelo_relacional_3_4_5_6

Requisitos 3, 4, 5 y 6 – Modelos relacionales, migraciones, consultas y aplicación MVC/CRUD

### ✔ Requisito 3 – Modelos con relaciones

Relaciones implementadas:

- Uno a Uno: PerfilCliente → Cliente

- Uno a Muchos: Pedido → Cliente

- Muchos a Muchos: Pedido ↔ Producto

### ✔ Requisito 4 – Migraciones

Uso de makemigrations y migrate para propagar cambios al esquema de la base de datos.

### ✔ Requisito 5 – Consultas ORM y SQL

Filtrado de datos con filter(), exclude(), get(), annotate().

Consultas SQL personalizadas mediante django.db.connection.cursor.

### ✔ Requisito 6 – Aplicación MVC con CRUD

Implementación de vistas, URLs y templates para:

- Listar productos

- Crear productos

- Editar productos

- Ver detalles

- Eliminar productos

Archivos relevantes:

- models.py (modelos relacionales)

- views.py, urls.py, templates/ (CRUD MVC)

- README.md (ejemplos de consultas y explicación de relaciones)

## 4️⃣ aplicaciones_preinstaladas_7

Requisito 7 – Reconocimiento de aplicaciones preinstaladas de Django

Explicación de la utilidad de las apps preinstaladas:

- django.contrib.admin → administración de modelos

- django.contrib.auth → gestión de usuarios y permisos

- django.contrib.sessions → manejo de sesiones

- Registro de modelos en el panel de administración (admin.site.register) para gestionar datos de manera gráfica.

Archivos relevantes:

- admin.py (registro de modelos)

- README.md (explicación de las aplicaciones y su uso)

## ⚡ Flujo de trabajo recomendado

1. Clonar el repositorio:
```bash
git clone <[url_del_repositorio](https://github.com/JATeR912/M7_Evaluacion_de_portafolio)>
cd nombre_proyecto
```

2. Crear y activar entorno virtual:
```bash
python -m venv myenv
source myenv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Configurar la base de datos en settings.py.

Ejecutar migraciones:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Crear superusuario para acceder al admin:
```bash
python manage.py createsuperuser
```

6. Ejecutar el servidor:
```bash
python manage.py runserver
```
## 📝 Notas

Cada carpeta incluye un README.md específico explicando el requisito que cumple.

Se recomienda seguir el orden numérico de carpetas para entender la progresión del proyecto y el uso del ORM.

Todas las consultas ORM se pueden probar directamente en la shell de Django (python manage.py shell).
