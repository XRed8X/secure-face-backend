from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Clase personalizada para el modelo de usuario en el admin
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'username', 'is_active', 'is_staff', 'date_joined')
    list_filter = ('is_active', 'is_staff')
    
    # Aseguramos que no se usen campos inexistentes
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'is_staff', 'is_active'),
        }),
    )
    
    # Eliminamos 'groups' y 'user_permissions' de filter_horizontal
    filter_horizontal = ()  # No se usan estos campos
    search_fields = ('email', 'username')
    readonly_fields = ('date_joined', 'last_login')
    
    # 'ordering' debe ser una lista o tupla
    ordering = ('email',)

# Registro del modelo en el admin
admin.site.register(CustomUser, CustomUserAdmin)
