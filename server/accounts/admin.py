from django.contrib import admin
from .models import User

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # list_display = [field.name for field in User._meta.fields if field.name != "id"]
    list_display = ("first_name", "last_name", "mobile_number", "email", "date_of_birth", "password")
