from django.contrib import admin

# Register your models here.
from .models import User
from django.contrib import admin
from .models import InternshipApplication
admin.site.register(InternshipApplication)

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'domain')
    search_fields = ('email', 'name', 'domain')
    readonly_fields = ('password',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(User, UserAdmin)



