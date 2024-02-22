from rest_framework.pagination import PageNumberPagination

class CustomPageNumberPagination(PageNumberPagination):
    def paginate_queryset(self, queryset, request, view=None):
        if 'page' in request.query_params:
            return super().paginate_queryset(queryset, request, view)
        return None
