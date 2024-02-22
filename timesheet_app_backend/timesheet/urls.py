from django.urls import path
from timesheet_app_backend.timesheet.view.category.category_first_letters_list_view import CategoryFirstLetterListView
from timesheet_app_backend.timesheet.view.category.category_list_create_view import CategoryListCreateView
from timesheet_app_backend.timesheet.view.category.category_retrieve_update_destroy_view import CategoryRetrieveUpdateDestroyView
from timesheet_app_backend.timesheet.view.client.client_first_letters_list_view import ClientFirstLetterListView
from timesheet_app_backend.timesheet.view.client.client_generic_view import ClientGenericView
from timesheet_app_backend.timesheet.view.employee.employee_generic_view import EmployeeGenericView
from timesheet_app_backend.timesheet.view.project.project_first_letters_list_view import ProjectFirstLetterListView
from timesheet_app_backend.timesheet.view.project.project_generic_view import ProjectGenericView
from timesheet_app_backend.timesheet.view.task.task_generic_view import TaskGenericView
from timesheet_app_backend.timesheet.view.task.task_day_sum_hours_view import TaskDaySumHoursView
from timesheet_app_backend.timesheet.view.task.task_month_sum_hours_view import TaskMonthSumHoursView
from timesheet_app_backend.timesheet.view.task.task_generate_pdf_view import TaskGeneratePdfView
from timesheet_app_backend.timesheet.view.task.task_generate_excel_pdf_view import TaskGenerateExcelView
from timesheet_app_backend.timesheet.view.task.task_search_list_view import TaskSearchListView
from timesheet_app_backend.timesheet.authentication.login_view import LoginView
from timesheet_app_backend.timesheet.authentication.logout_view import LogoutView
from timesheet_app_backend.timesheet.authentication.forgot_password_view import ForgotPasswordView
from timesheet_app_backend.timesheet.authentication.get_user_by_token_view import GetUserByTokenView

urlpatterns = [
    path('authentication/login', LoginView.as_view()),
    path('authentication/logout', LogoutView.as_view()),
    path('authentication/forgot_password', ForgotPasswordView.as_view()),
    path('authentication/get_user/<str:token>', GetUserByTokenView.as_view()),
    path('categories', CategoryListCreateView.as_view()),
    path("categories/<int:pk>", CategoryRetrieveUpdateDestroyView.as_view()),
    path("categories/first_letters", CategoryFirstLetterListView.as_view()),
    path("clients", ClientGenericView.as_view()),
    path("clients/<int:pk>", ClientGenericView.as_view()),
    path("clients/first_letters", ClientFirstLetterListView.as_view()),
    path("projects", ProjectGenericView.as_view()),
    path("projects/<int:pk>", ProjectGenericView.as_view()),
    path("projects/first_letters", ProjectFirstLetterListView.as_view()),
    path("employees", EmployeeGenericView.as_view()),
    path("employees/<int:pk>", EmployeeGenericView.as_view()),
    path("tasks", TaskGenericView.as_view()),
    path("tasks/<int:pk>", TaskGenericView.as_view()),
    path("tasks/day_sum_hours",TaskDaySumHoursView.as_view()),
    path("tasks/month_sum_hours", TaskMonthSumHoursView.as_view()),
    path("tasks/pdf", TaskGeneratePdfView.as_view()),
    path("tasks/excel",TaskGenerateExcelView.as_view()),
    path("tasks/search", TaskSearchListView.as_view()),
]