
from django.conf.urls import include, url
from django.contrib import admin
#from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('sales.urls')),
]

#urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
