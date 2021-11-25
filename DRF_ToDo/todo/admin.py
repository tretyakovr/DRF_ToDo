from django.contrib import admin
from .models import Projects, Roles, ProjectUsers, Todo

admin.site.register(Projects)
admin.site.register(Roles)
admin.site.register(ProjectUsers)
admin.site.register(Todo)
