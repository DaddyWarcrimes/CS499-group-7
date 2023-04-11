from django.contrib import admin
from .models import employee,product,orderItem,purchaseOrder,shipmentIn,shipmentOut,manifest,manifestItem,vehicle,part,partsList

class adminEmployee(admin.ModelAdmin):
    list_display = ['username','lName','fName','mName']

# Register your models here.

admin.site.register(employee,adminEmployee)
admin.site.register(product)
admin.site.register(orderItem)
admin.site.register(purchaseOrder)
admin.site.register(shipmentIn)
admin.site.register(shipmentOut)  
admin.site.register(manifest)
admin.site.register(manifestItem)  
admin.site.register(vehicle)
admin.site.register(part) 
admin.site.register(partsList)  

#Template for copypasta
#admin.site.register(<++>)  
