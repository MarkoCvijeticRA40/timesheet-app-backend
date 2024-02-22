from datetime import datetime
from django.db.models import Sum
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from timesheet_app_backend.timesheet.model.task import Task

class TaskMonthSumHoursView(APIView):

    def get(self, request, *args, **kwargs):
        month = request.query_params.get('month')
        year = request.query_params.get('year')
        employee_id = request.query_params.get('employee_id')
        if not (month and year and employee_id):
            return Response("Month, year, or employee_id parameter is missing.", status=HTTP_400_BAD_REQUEST)
        try:
            date = datetime(int(year), int(month), 1)
        except ValueError:
            return Response("Invalid month or year value.", status=HTTP_400_BAD_REQUEST)
        queryset = Task.objects.filter(employee_id=employee_id, date__month=month, date__year=year)
        result = queryset.aggregate(total_hours=Sum('hours') + Sum('overtime'))
        total_hours = result['total_hours'] or 0
        return Response(total_hours, status=HTTP_200_OK)
