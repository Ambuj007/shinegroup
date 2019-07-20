from django.contrib import admin
from .models import Stock
# Register your models here.

class StockAdmin(admin.ModelAdmin):
    list_display = ('id','category','brand','item','typep','specificationp','Model_No','purchase_price','selling_price')
    list_editable = ('selling_price',)
    list_per_page = 10
    search_fields = ('category','brand','typep','specificationp','Model_No')
    list_filter = ('category','typep','specificationp')

admin.site.register(Stock, StockAdmin)


admin.site.site_header = "Shine Computer"
admin.site.site_title = "Shine Enterprises"
admin.site.index_title = "Inventory Manager"