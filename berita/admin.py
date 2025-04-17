from django.contrib import admin
from berita.models import Kategori, Artikel

# Register your models here.

admin.site.register(Kategori)

class Artikeladmin(admin.ModelAdmin):
    list_display = ['judul','kategori','author']
    search_fields = ['judul']
admin.site.register(Artikel, Artikeladmin)