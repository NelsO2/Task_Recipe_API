from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from main import models

# Register your models here.




admin.site.register(models.User, UserAdmin),
admin.site.register(models.Recipe),
admin.site.register(models.Tag),
admin.site.register(models.Ingredient),