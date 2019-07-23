from django.contrib import admin
from .models import Stock
# Register your models here.

class StockAdmin(admin.ModelAdmin):
    list_display = ('id','category','brand','item','item_type','item_specification','model_no','purchase_price','selling_price')
    list_editable = ('selling_price',)
    list_per_page = 10
    search_fields = ('category','brand','item_type','item_specification','model_no')
    list_filter = ('category','item_type','item_specification')

admin.site.register(Stock, StockAdmin)


admin.site.site_header = "Shine Computer"
admin.site.site_title = "Shine Enterprises"
admin.site.index_title = "Inventory Manager"