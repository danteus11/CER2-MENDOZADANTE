#el encargado de recibir las peticiones de los usuarios, consultar los datos en los modelos que acabamos de ver y decidir que plantilla HTML se va a mostrar en pantalla
from django.shortcuts import render, get_object_or_404
from .models import LugarPatrimonial, Categoria

# Vista para renderizar la página de bienvenida o inicio del sitio
def home_view(request):
    #Retorna directamente la plantilla de la pagina de inicio sin necesidad de consultar datos complejos a la base de datos.
    return render(request, 'core/home.html')

#Define la vista encargada de mostrar el listado y los filtros del catalogo patrimonial
def catalogo_view(request):
    #Obtiene todas las categorías disponibles en la base de datos para mostrarlas en la barra lateral de filtros
    categorias = Categoria.objects.all()
    #Revisa si el usuario hizo clic en algún filtro de categoría en la URL
    categoria_id = request.GET.get('categoria')
    
    if categoria_id:
        # Filtra por la categoría seleccionada 
        lugares = LugarPatrimonial.objects.filter(categoria_id=categoria_id)
    else:
        # Muestra todos los lugares si no hay filtro 
        lugares = LugarPatrimonial.objects.all()

    #diccionario, empaqueta la lista    
    context = {
        'lugares': lugares,
        'categorias': categorias,
        'categoria_seleccionada': categoria_id
    }
    #procesa la petición web combinándola con la plantilla catalogo.html y le inyecta todo el diccionario context empaquetado y ordenado
    return render(request, 'core/catalogo.html', context)

# Para que se vea mas limpio si hay una falla
def detalle_lugar_view(request, lugar_id):
    lugar = get_object_or_404(LugarPatrimonial, pk=lugar_id)
    return render(request, 'core/detalle_lugar.html', {'lugar': lugar})
