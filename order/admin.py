from django.contrib import admin

from .models import Order, OrderItems


class OrderItemInline(admin.TabularInline):
    model = OrderItems
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'created_at']
    list_filter = ['status', 'created_at']

    search_fields = ['first_name', 'address']
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItems)
