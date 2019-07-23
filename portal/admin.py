from django.contrib import admin
from . models import CustomUser,Request,Profile

admin.site.register(CustomUser)
admin.site.register(Request)
admin.site.register(Profile)
