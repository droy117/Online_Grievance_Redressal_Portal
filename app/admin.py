from django.contrib import admin

from .models import User, Grievance

admin.site.site_header = "OGRP Admin Interface"
admin.site.site_title = "OGRP Admin Portal"
admin.site.index_title = "Welcome to OGPR Admin Panel"

admin.site.register(User)
admin.site.register(Grievance)