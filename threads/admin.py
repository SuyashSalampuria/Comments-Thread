from django.contrib import admin
from .models import ParentMessage, ThreadMessage, Page

# Register all the models here

admin.site.register(Page)
admin.site.register(ParentMessage)
admin.site.register(ThreadMessage)