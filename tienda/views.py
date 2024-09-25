from django.shortcuts import get_object_or_404, render
from .models import Producto
from .models import Categoria
def index(request):
    categorias = Categoria.objects.all()  
    productos = Producto.objects.all()     
    return render(request, 'index.html', {'categorias': categorias, 'product_list': productos})

def producto(request,producto_id):
    producto= get_object_or_404(Producto, pk=producto_id)
    return render(request,'producto.html',{'producto':producto})

    
def categoria_productos(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id) 
    productos = Producto.objects.filter(categoria=categoria)   
    return render(request, 'categoria_productos.html', {'categoria': categoria, 'productos': productos})