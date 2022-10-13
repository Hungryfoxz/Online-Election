from email.headerregistry import Group
from unicodedata import name
from django.contrib import admin
from home.models import Contact,Student_Registration,Positions,Candidate,Logged,sms


# Register your models here.
admin.site.register(Contact)
admin.site.register(Student_Registration)
admin.site.register(Positions)
admin.site.register(Candidate)
admin.site.register(Logged)
admin.site.register(sms)
