from django.contrib import admin
from .models import Record, Platform, RecordType, Account, Post

# Register your models here.
admin.site.register(Record)
admin.site.register(Platform)
admin.site.register(RecordType)
admin.site.register(Account)
admin.site.register(Post)