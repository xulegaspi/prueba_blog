from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from django.contrib import admin
from Blog import views

urlpatterns = patterns('prueba_blog.Blog.views',

    url(r'^Blog/', views.main),

    # Examples:
    # url(r'^$', 'prueba_blog.views.home', name='home'),
    # url(r'^prueba_blog/', include('prueba_blog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    #urlpatterns = patterns()
)
