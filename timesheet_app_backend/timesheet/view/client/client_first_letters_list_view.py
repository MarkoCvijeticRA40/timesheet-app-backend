from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from timesheet_app_backend.timesheet.model.client import Client

class ClientFirstLetterListView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Client.objects.values_list('name', flat=True)
        first_letters = {name[0].lower() for name in queryset if name}
        return Response(list(first_letters), status=HTTP_200_OK)
