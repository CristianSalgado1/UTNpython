from django.conf.urls import url
from vistaprevia import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^cargar/',  views.cargar_imagen,  name = "cargar"), 
    url(r'^(?P<producto_id>\d+)/ver/$',  views.ver_imagen,  name = "ver"), 
    url(r'^verimagenes/$',  views.ver_imagenes,  name = "verimagenes")
]
