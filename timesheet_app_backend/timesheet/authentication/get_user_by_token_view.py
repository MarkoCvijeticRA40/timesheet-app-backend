from datetime import timedelta

from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from timesheet_app_backend.timesheet.serializer.employee_serializer import EmployeeSerializer

class GetUserByTokenView(APIView):

    def is_valid_token(self, user):
        existing_token = Token.objects.filter(user=user).first()
        if existing_token:
            current_time = timezone.localtime(timezone.now())
            return current_time <= existing_token.created + timedelta(hours=2)
        return False

    def get(self, request, token):
        try:
            token_obj = Token.objects.get(key=token)
            user = token_obj.user
            if not self.is_valid_token(user):
                return Response({'message': 'Token expired'}, status=status.HTTP_401_UNAUTHORIZED)
            serializer = EmployeeSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            return Response({'message': 'Token not found'}, status=status.HTTP_404_NOT_FOUND)