from django.contrib import admin
from . models import categoryTable, cardTable, cardTableNew

# Register your models here.

admin.site.register(categoryTable)
admin.site.register(cardTableNew)
admin.site.register(cardTable)