from rest_framework import pagination


class CustomPagination(pagination.PageNumberPagination):
    page_size = 20
    max_page_size = 50
    page_size_query_param = 'limit'
