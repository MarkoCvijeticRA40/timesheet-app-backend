from django.http import HttpResponse
from rest_framework.views import APIView
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from timesheet_app_backend.timesheet.model.category import Category
from timesheet_app_backend.timesheet.model.employee import Employee
from timesheet_app_backend.timesheet.model.project import Project

class TaskGeneratePdfView(APIView):

    def post(self, request):
        tasks = request.data.get('tasks', [])
        data = [['Date', 'Employees', 'Projects', 'Categories', 'Description', 'Time']]
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
            print(request.data.get('time'))
            time_value = task.get('hours') + task.get('overtime') if request.GET.get('time') == 'time' else task.get('overtime')
            data.append([
                task.get('date', ''),
                employee_name,
                project_name,
                category_name,
                task.get('description', ''),
                time_value
            ])
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="tasks.pdf"'
        doc = SimpleDocTemplate(response, pagesize=letter)
        table = Table(data)
        style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                            ('GRID', (0, 0), (-1, -1), 1, colors.black)])

        table.setStyle(style)
        doc.build([table])
        return response