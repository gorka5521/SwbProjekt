from django.contrib import admin

# Register your models here.
from leage.models import Postac, Rola, Pozycja

from leage.models import *

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(Order)

admin.site.register(Postac)
admin.site.register(Rola)
admin.site.register(Pozycja)
