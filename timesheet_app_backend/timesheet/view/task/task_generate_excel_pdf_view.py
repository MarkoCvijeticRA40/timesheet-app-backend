from django.http import HttpResponse
from openpyxl import Workbook
from rest_framework.views import APIView
from timesheet_app_backend.timesheet.model.category import Category
from timesheet_app_backend.timesheet.model.employee import Employee
from timesheet_app_backend.timesheet.model.project import Project

class TaskGenerateExcelView(APIView):

    def post(self, request):
        tasks = request.data.get('tasks', [])
        wb = Workbook()
        ws = wb.active
        headers = ['Date', 'Employee', 'Project', 'Category', 'Description', 'Time']
        ws.append(headers)
        for task in tasks:
            employee_id = task.get('employee_id')
            employee = Employee.objects.get(id=employee_id)
            employee_name = employee.name
            project_id = task.get('project_id')
            project = Project.objects.get(id=project_id)
            project_name = project.name
            category_id = task.get('category_id')
            category = Category.objects.get(id=category_id)
            category_name = category.name
            time_value = task.get('hours') + task.get('overtime') if request.GET.get('time') == 'time' else task.get('overtime')
            row_data = [
                task.get('date', ''),
                employee_name,
                project_name,
                category_name,
                task.get('description', ''),
                time_value
            ]
            ws.append(row_data)
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="tasks.xlsx"'
        wb.save(response)
        return response