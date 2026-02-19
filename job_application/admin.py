from django.contrib import admin
from .models import Database_From


class Database_FromAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "email",
    )
    search_fields = (
        "first_name",
        "last_name",
        "email",
    )
    list_filter = (
        "date",
        "occupation",
    )
    ordering = ("first_name",)
    # make one field 'read only'
    readonly_fields = ("occupation",)


admin.site.register(Database_From, Database_FromAdmin)
