from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from timesheet_app_backend.timesheet.model.task import Task
from django.db.models import Sum

class TaskDaySumHoursView(APIView):

    def get(self, request, *args, **kwargs):
        date = request.query_params.get('date')
        employee_id = request.query_params.get('employee_id')
        if not employee_id:
            return Response("Employee_id parameter is missing.", status=HTTP_400_BAD_REQUEST)
        queryset = Task.objects.filter(employee_id=employee_id)
        if date:
            queryset = queryset.filter(date=date)
        result = queryset.aggregate(total_hours=Sum('hours') + Sum('overtime'))
        total_hours = result['total_hours'] or 0
        response_data = {'date': date,'employee_id': employee_id,'total_hours': total_hours
        }
        return Response(response_data, status=HTTP_200_OK)