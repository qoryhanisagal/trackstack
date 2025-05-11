from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        'username', 
        'last_name',
        'first_name',
        'role', 
        'team', 
        'last_login',
        'is_staff'
    ]
    add_fieldsets = UserAdmin.fieldsets + (
        (
            None, {
                'classes': ('wide',),
                'fields': ('username', 'email', 'role', 'team', 'password1', 'password2')
            }
        ),
    )
    fieldsets = UserAdmin.fieldsets + (
        (
            None, {'fields': ('role', 'team')}
        ),

    )


admin.site.register(CustomUser, CustomUserAdmin)