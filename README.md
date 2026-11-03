# CER2-MENDOZADANTE - Fundación Patrimonio Vivo

Aplicación web desarrollada con Python y Django Framework para la gestión y visualización de un catálogo digital de lugares de interés patrimonial.

## Tecnologías Utilizadas
- Python 3.11+
- Django 5.x / 5.2
- Bootstrap 5 (recursos estáticos locales)
- SQLite (Base de datos por defecto)

---

## Instrucciones de Instalación y Ejecución

Sigue estos pasos en tu terminal para clonar, configurar y ejecutar el proyecto localmente:

1. Clonar el repositorio:
   git clone https://github.com/danteus11/CER2-MENDOZADANTE.git
   cd CER2_MENDOZADANTE

2. Instalar las dependencias:
   pip install -r requirements.txt

3. Aplicar las migraciones a la base de datos:
   python manage.py makemigrations
   python manage.py migrate

4. Crear un usuario administrador:
   python manage.py createsuperuser

5. Ejecutar el servidor de desarrollo:
   python manage.py runserver

---

## Panel de Administración y Pruebas
- Para probar la sección de gestión protegida, ingresa a `/admin/` en el navegador y utiliza las credenciales del usuario administrador creado en el paso 4.
- Desde allí podrás agregar, modificar y eliminar categorías y lugares patrimoniales.
- Los visitantes generales pueden navegar libremente por la página principal, el catálogo dinámico, los filtros por categoría y la vista de detalle de cada lugar.