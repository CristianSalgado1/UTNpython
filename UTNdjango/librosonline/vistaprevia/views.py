from django.shortcuts import render
from vistaprevia.models import Productos
from django.shortcuts import redirect
from vistaprevia.forms import CargarForm

from django.shortcuts import  render_to_response
from django.http import Http404
from django.template import RequestContext
    
def index(request):
    contenido = {'nombre_sitio': 'LibrosOnline'}
    para_minorista = {'tipo_usuario': 'minorista', 'incremento': '25'}
    para_mayorista = {'tipo_usuario': 'mayorista', 'incremento': '10'}
    return render(request,  'vistaprevia/index.html',  {'contenido': contenido,  'para_minorista': para_minorista,  'para_mayorista': para_mayorista})



def cargar_imagen(request):
    if request.method == 'POST':
        form = CargarForm(request.POST,  request.FILES)
        
        if form.is_valid():
            newdoc = Productos(producto = request.POST['producto'],  ruta_imagen = request.FILES['ruta_imagen'])
            newdoc.save(form)
            return redirect('index')
            #return HttpResponse
    else:
        form = CargarForm()
    return render(request,  'vistaprevia/formulario.html',  {'form':form})
    
        
def ver_imagen(request,  producto_id):
    try:
        producto = Productos.objects.get(pk = producto_id)
    except Productos.DoesNotExist:
        raise Http404
    return render_to_response('vistaprevia/verimagen.html',  
        {'producto': producto, 
        'error_message' :  "No has seleccionado un producto." }, 
        content_type = RequestContext(request)
        )
        
def ver_imagenes(request):
    try:
        productos =  Productos.objects.all()
    except Productos.DoesNotExist:
        raise Http404
    return render_to_response('vistaprevia/verimagenes.html',  {
        'productos': productos, 
        'error_message':"No has seleccionado un producto"
            }, content_type = RequestContext(request) 
            )
