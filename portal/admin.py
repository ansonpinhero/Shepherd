from django.contrib import admin
from . models import CustomUser,Request,Profile,volunteer_invitations

admin.site.register(CustomUser)
admin.site.register(Request)
admin.site.register(volunteer_invitations)
admin.site.register(Profile)
