from django.contrib import admin
from timebook.models import *

# Register your models here.


class JobAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Customer',    {'fields': ['customer']}),
        (None,      {'fields': ['order_number']}),
        (None,      {'fields': ['description']}),
    ]


admin.site.register(Customer)
admin.site.register(Job, JobAdmin)
admin.site.register(TimeType)
admin.site.register(Worker)
admin.site.register(Time)
