from django.contrib import admin
from django.contrib.auth.models import User


from .models import Menu
from .models import MenuCategory
# from .models import Logger

# Register your models here.

admin.site.register(Menu)
admin.site.register(MenuCategory)

# admin.site.register(Logger)