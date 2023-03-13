from django.contrib import admin

#  we must tell admin about our custom user model which we have created in core app and override default user model so default user is now showing in admin panel so we need to register here our custom user 
from django.contrib.auth.admin import UserAdmin  as BaseUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # we take this code from useradmin which we import from admin
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2" ,"email" , 'first_name','last_name' ),
            },
        ),
    )