from django.shortcuts import render, get_object_or_404
from .models import LugarPatrimonial, Categoria

def home_view(request):
    return render(request, 'core/home.html')

def catalogo_view(request):
    categorias = Categoria.objects.all()
    categoria_id = request.GET.get('categoria')
    
    if categoria_id:
        # Filtra por la categoría seleccionada 
        lugares = LugarPatrimonial.objects.filter(categoria_id=categoria_id)
    else:
        # Muestra todos los lugares si no hay filtro 
        lugares = LugarPatrimonial.objects.all()
        
    context = {
        'lugares': lugares,
        'categorias': categorias,
        'categoria_seleccionada': categoria_id
    }
    return render(request, 'core/catalogo.html', context)

# Para que se vea mas limpio si hay una falla
def detalle_lugar_view(request, lugar_id):
    lugar = get_object_or_404(LugarPatrimonial, pk=lugar_id)
    return render(request, 'core/detalle_lugar.html', {'lugar': lugar})
