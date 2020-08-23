from django.contrib import admin
from .models import ( 
    Advisory, Supplier, Instruction,
    InventoryItemType, InventoryItem, InventoryItemSupplier, InventoryMovementLog,
    Request, RequestItem, Delivery, ReceivedItem,
    Depletion, DepletionItem, DepletionDepletionItem
)

# Register your models here.

admin.site.register(Advisory)
admin.site.register(Instruction)
admin.site.register(Supplier)
admin.site.register(InventoryItem)
admin.site.register(InventoryItemType)
admin.site.register(InventoryItemSupplier)
admin.site.register(InventoryMovementLog)
admin.site.register(Request)
admin.site.register(RequestItem)
admin.site.register(Delivery) 
admin.site.register(ReceivedItem)
admin.site.register(Depletion)
admin.site.register(DepletionItem)
admin.site.register(DepletionDepletionItem)