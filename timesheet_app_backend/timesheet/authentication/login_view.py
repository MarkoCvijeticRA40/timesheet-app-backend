from django.contrib.auth import login
from django.contrib.auth.hashers import check_password
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from timesheet_app_backend.timesheet.model.employee import Employee

class LoginView(APIView):

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            user = Employee.objects.get(email=email)
        except Employee.DoesNotExist:
            return JsonResponse({'message': 'Invalid credentials'}, status=400)
        if check_password(password, user.password):
            login(request, user)
            existing_token = Token.objects.filter(user=user).first()
            if existing_token:
                return JsonResponse(
                    {'message': 'Login successful', 'token': existing_token.key, 'role': user.role})
            else:
                new_token = Token.objects.create(user=user)
                return JsonResponse({'message': 'Login successful', 'token': new_token.key, 'role': user.role})
        else:
            return JsonResponse({'message': 'Invalid credentials'}, status=400)
