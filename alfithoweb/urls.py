from django.contrib import admin
from django.urls import path

#menampilkan gambar yang sudah di upload di folder media#
from django.conf import settings
from django.conf.urls.static import static


from alfithoweb.views import home, about, kutipan
urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', home, name="home"),
    path('about/', about, name="about"),
    path('kutipan/', kutipan, name="kutipan"),
]

#menampilkan gambar yang sudah di upload di folder media#
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)