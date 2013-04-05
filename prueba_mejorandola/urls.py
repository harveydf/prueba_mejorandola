from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from prueba_mejorandola import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

modulos = ('restaurante', 'cancion')

# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'prueba_mejorandola.views.home', name='home'),
#     # url(r'^prueba_mejorandola/', include('prueba_mejorandola.foo.urls')),

#     # Uncomment the admin/doc line below to enable admin documentation:
#     # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

#     # Uncomment the next line to enable the admin:
#     # url(r'^admin/', include(admin.site.urls)),
# )

urlpatterns = patterns('',
    url(r'^$', 'core.views.home'),
   *(url(r'^%s/$'%modulo, '%s.views.show_%s'%(modulo,modulo)) for modulo in modulos)
)

urlpatterns += patterns('',
   *(url(r'^%s/(?P<id>\d+)/$'%modulo, '%s.views.cargar_%s'%(modulo,modulo)) for modulo in modulos)
)

urlpatterns += patterns('',
   *(url(r'^%s/eliminar/(?P<id>\d+)/$'%modulo, '%s.views.eliminar_%s'%(modulo,modulo)) for modulo in modulos)
)


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)