from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from timesheet_app_backend.timesheet.model.category import Category
from timesheet_app_backend.timesheet.serializer.category_serializer import CategorySerializer
from timesheet_app_backend.timesheet.page_number_pagination import CustomPageNumberPagination
from django.db.models import Q

class CategoryListCreateView(ListCreateAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        first_letter = self.request.query_params.get('first_letter', '')
        search_term = self.request.query_params.get('search_input', '')
        pk_param = self.request.query_params.get('pk', '')
        combined_query = Q()
        if first_letter:
            combined_query &= Q(name__istartswith=first_letter)
        if search_term:
            combined_query &= Q(name__icontains=search_term)
        if pk_param:
            combined_query &= Q(pk=pk_param)
        queryset = queryset.filter(combined_query)
        return queryset

    def list(self, request, *args, **kwargs):
        page_param = self.request.query_params.get('page')
        print(page_param)
        if page_param is not None:
            try:
                page_number = int(page_param)
                self.pagination_class.page = page_number
            except ValueError:
                pass
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        else:
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data, status=HTTP_200_OK)
