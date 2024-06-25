from django.contrib import admin
from .models import Notes
from django.contrib.auth.models import Permission
# Register your models here.

class NotesAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Description', 'uploadingdate', 'File')  # Add 'get_file'
    def File(self, obj):
        return obj.File.url  # Return the URL of the uploaded file

admin.site.register(Notes, NotesAdmin)

