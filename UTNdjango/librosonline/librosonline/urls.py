from django.conf.urls import url, include

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
     url(r'^vistaprevia/',  include('vistaprevia.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
