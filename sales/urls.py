from django.conf.urls import *
from sales import views
from django.conf import settings
from django.contrib import admin
#from django.conf.urls.static import static
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = [
    url(r'^$', views.index, name='index'),
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#urlpatterns += staticfiles_urlpatterns()
