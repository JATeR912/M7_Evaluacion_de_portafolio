## ✅ 1. Integración del framework Django con bases de datos

Django integra bases de datos utilizando su ORM (Object-Relational Mapper), el cual permite trabajar con tablas y registros usando código Python en lugar de SQL directamente.

Esto facilita:

- Crear modelos → Django genera tablas automáticamente

- Realizar consultas → sin escribir SQL

- Mantener portabilidad → cambiar de base de datos sin cambiar el código del proyecto

Django soporta varios motores de base de datos como:

- SQLite (por defecto)

- MySQL

- PostgreSQL

- Otros mediante extensiones

### ¿Cómo Django maneja las conexiones con la base de datos?

Django gestiona automáticamente:

✔ Conexiones

Abre, reutiliza o cierra conexiones según sea necesario.

✔ Operaciones de lectura y escritura

El ORM traduce código Python a SQL para:

- INSERT

- SELECT

- UPDATE

- DELETE

Ejemplo:
```bash
Producto.objects.filter(precio__gte=5000)
```

Esto se convierte internamente en SQL sin que el desarrollador lo escriba.

✔ Control de migraciones

Las migraciones actualizan la base de datos basadas en los modelos:
```bash
python manage.py makemigrations
python manage.py migrate
```
### Configuración de la base de datos en settings.py

El archivo settings.py contiene la sección DATABASES, donde se define el motor a utilizar.

A continuación se explican las configuraciones para SQLite, MySQL y PostgreSQL.

#### A) Configuración para SQLite (Predeterminada)

No requiere instalación adicional.
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
##### ✔ Características:

Base de datos por defecto de Django.

No requiere servidor ni configuraciones adicionales.

Ideal para proyectos pequeños o educativos.

#### B) Configuración para MySQL
##### 🔧 Instalación del conector

Puedes instalar mysqlclient (oficial y recomendado):
```bash
pip install mysqlclient
```

O instalar PyMySQL como alternativa:
```bash
pip install pymysql
```

Si usas PyMySQL, debes añadir en __init__.py del proyecto:
```bash
import pymysql
pymysql.install_as_MySQLdb()
```
##### 🔧 Configuración en settings.py
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nombre_db',          # Nombre de la base de datos
        'USER': 'tu_usuario',         # Usuario MySQL
        'PASSWORD': 'tu_contraseña',  # Contraseña
        'HOST': 'localhost',          # Servidor MySQL
        'PORT': '3306',               # Puerto por defecto
    }
}
```
##### ✔ Características:

Ideal para aplicaciones medianas o grandes.

Requiere servidor MySQL funcionando.

#### C) Configuración para PostgreSQL
##### 🔧 Instalación del conector
```bash
pip install psycopg2
```
(Alternativa: psycopg2-binary para entornos locales)

##### 🔧 Configuración en settings.py
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'database_name',
        'USER': 'postgres',
        'PASSWORD': 'contraseña',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
##### ✔ Características:

Más robusto que MySQL en integridad de datos.

Recomendado para producción.