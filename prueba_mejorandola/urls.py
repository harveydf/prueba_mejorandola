from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'prueba_mejorandola.views.home', name='home'),
    # url(r'^prueba_mejorandola/', include('prueba_mejorandola.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'core.views.home'),
    url(r'^restaurante/$', 'restaurante.views.show_restaurantes'),
    url(r'^restaurante/(?P<id>\d+)/$', 'restaurante.views.cargar_restaurante'),
    url(r'^restaurante/eliminar/(?P<id>\d+)/$', 'restaurante.views.eliminar_restaurante'),
)
