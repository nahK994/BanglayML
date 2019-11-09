from django.contrib import admin
from . models import categoryTable, card_table, image_table, image_list_table

admin.site.register(categoryTable)
admin.site.register(card_table)
admin.site.register(image_table)
admin.site.register(image_list_table)