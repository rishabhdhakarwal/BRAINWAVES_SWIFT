from django.contrib import admin

# Register your models here.
from .models import ClientOneToOne
from .models import *

admin.site.register(ClientOneToOne)
admin.site.register(SgOneToOne)
admin.site.register(matched)
