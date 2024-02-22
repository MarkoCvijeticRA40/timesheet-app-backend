from dateutil.parser import parse
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView
from timesheet_app_backend.timesheet.model.task import Task
from timesheet_app_backend.timesheet.serializer.task_serializer import TaskSerializer

class TaskSearchListView(APIView):

    def get(self, request):
        client_id = request.query_params.get('client_id')
        project_id = request.query_params.get('project_id')
        category_id = request.query_params.get('category_id')
        employee_id = request.query_params.get('employee_id')
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')
        start_date = parse(start_date).date() if start_date else None
        end_date = parse(end_date).date() if end_date else None
        queryset = Task.objects.all()
        q_objects = Q()
        if not any([client_id, project_id, category_id, employee_id, start_date, end_date]):
            return Response([])
        if client_id:
            q_objects &= Q(client_id=int(client_id))
        if project_id:
            q_objects &= Q(project_id=int(project_id))
        if category_id:
            q_objects &= Q(category_id=int(category_id))
        if employee_id:
            q_objects &= Q(employee_id=int(employee_id))
        if start_date and end_date:
            q_objects &= Q(date__range=[start_date, end_date])
        elif start_date:
            q_objects &= Q(date__gte=start_date)
        elif end_date:
            q_objects &= Q(date__lte=end_date)
        queryset = queryset.filter(q_objects).order_by('-date')
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)