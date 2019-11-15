from django.contrib import admin
from . models import Categories, CardsInfo, Images, Codes, Recommendations

admin.site.register(Categories)
admin.site.register(CardsInfo)
admin.site.register(Images)
admin.site.register(Codes)
admin.site.register(Recommendations)