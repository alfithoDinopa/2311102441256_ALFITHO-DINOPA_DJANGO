from django.contrib import admin
from django.urls import path


from alfithoweb.views import home, about, kutipan
urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', home, name="home"),
    path('about/', about, name="about"),
    path('kutipan/', kutipan, name="kutipan"),
]
