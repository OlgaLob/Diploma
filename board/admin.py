from django.contrib import admin
from .models import User, Task, SignIn, Status

admin.site.register(User)
admin.site.register(Task)
admin.site.register(SignIn)
admin.site.register(Status)
