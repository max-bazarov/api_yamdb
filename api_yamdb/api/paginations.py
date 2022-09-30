from rest_framework.pagination import PageNumberPagination


class ClassPagination(PageNumberPagination):
    page_size = 10