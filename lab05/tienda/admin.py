from django.contrib import admin

from .models import Categoria,Producto,Cliente

class CambiarStock(admin.ModelAdmin):
    list_display = ["nombre", "stock"]
    actions = ["change_stock"]
  
    def change_stock(modeladmin, request, queryset):
        queryset.update(stock=20)
    change_stock.short_description = "Cambiar stock a 20"


admin.site.register(Producto,CambiarStock)
admin.site.register(Categoria)
admin.site.register(Cliente)
