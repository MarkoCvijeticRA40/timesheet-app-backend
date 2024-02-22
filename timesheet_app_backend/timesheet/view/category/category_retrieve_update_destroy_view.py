from rest_framework.generics import RetrieveUpdateDestroyAPIView
from timesheet_app_backend.timesheet.model.category import Category
from timesheet_app_backend.timesheet.serializer.category_serializer import CategorySerializer

class CategoryRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

