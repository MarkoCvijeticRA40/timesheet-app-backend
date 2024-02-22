from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from timesheet_app_backend.timesheet.model.employee import Employee

class ForgotPasswordView(APIView):

    def patch(self, request, *args, **kwargs):
        email = request.data.get('email')
        try:
            employee = Employee.objects.get(email=email)
        except Employee.DoesNotExist:
            return Response({'message': 'Employee with provided email does not exist'},
                            status=status.HTTP_404_NOT_FOUND)
        random_password = get_random_string(length=12)
        print("Random password:", random_password)
        send_mail(
            "Password Reset",
            f"Your new password is: {random_password}",
            "markopraksa@gmail.com",
            [email],
            fail_silently=False,
        )
        employee.set_password(random_password)
        employee.save()
        return Response({'message': 'Password reset successful'}, status=status.HTTP_200_OK)
