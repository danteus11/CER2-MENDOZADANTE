# CER2-MENDOZADANTE - Fundación Patrimonio Vivo

Aplicación web desarrollada con Python y Django Framework para la gestión y visualización de un catálogo digital de lugares de interés patrimonial, cumpliendo con los requerimientos del Certamen 2.

## Tecnologías Utilizadas
- Python 3.11+
- Django 5.x / 5.2
- Bootstrap 5 (recursos estáticos locales)
- SQLite (Base de datos por defecto)


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

4. Crear un superusuario (Administrador):
   python manage.py createsuperuser

5. Ejecutar el servidor de desarrollo:
   python manage.py runserver

---

## Usuarios y Permisos para Pruebas
- Panel de Administración (Gestión Protegida - RF10, RF11, RF12): Accede mediante /admin/ utilizando las credenciales del superusuario creado en el paso 4.
- Desde el panel de administración se pueden registrar, modificar y eliminar tanto Categorías como Lugares Patrimoniales.
- Los visitantes anónimos tienen acceso libre a la Página Principal (RF01), el Catálogo Dinámico (RF02), los Filtros por Categoría (RF04, RF05) y la Vista de Detalle Individual (RF03).