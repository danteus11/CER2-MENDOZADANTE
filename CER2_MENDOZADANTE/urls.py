"""
URL configuration for CER2_MENDOZADANTE project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import home_view, catalogo_view, detalle_lugar_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    #Habilita la ruta para acceder al panel de administración
    path('admin/', admin.site.urls),
    #Define la ruta principal o raíz del sitio web
    path('', home_view, name='home'),
    #Crea la ruta para mostrar el listado de espacios patrimoniales y sus filtros
    path('catalogo/', catalogo_view, name='catalogo'),
    #Crea una ruta dinámica que recibe un número entero para mostrar la página de detalles de un lugar específico
    path('lugar/<int:lugar_id>/', detalle_lugar_view, name='detalle_lugar'),
    # Rutas de Autenticación 
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]

