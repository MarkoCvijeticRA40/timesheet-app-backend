from django.contrib import admin
from .model.client import Client
from .model.employee import Employee
from .model.project import Project
from .model.task import Task
from .models import Category

class CategoryAdmin(admin.ModelAdmin):

    list_display = ('id', 'name')

class ClientAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'address', 'city', 'postal_code', 'country')

class ProjectAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'description', 'client_id', 'lead_id', 'status')

class EmployeeAdmin(admin.ModelAdmin):

   list_display = ('id', 'name', 'username', 'email', 'hours_per_week', 'status', 'role', 'password')
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_id', 'client_id', 'category_id', 'description', 'hours', 'overtime', 'employee_id', 'date')

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Task,TaskAdmin)