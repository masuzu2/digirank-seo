from django.contrib import admin
from myapp.models import Person, Client

admin.site.register(Person)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'website', 'package', 'budget', 'status', 'date')
    list_filter = ('package', 'status')
    search_fields = ('company_name', 'website')
