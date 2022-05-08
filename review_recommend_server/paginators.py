from rest_framework.pagination import PageNumberPagination


class BasePagination(PageNumberPagination):
    pageSize = 6
