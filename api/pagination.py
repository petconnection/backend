from rest_framework import pagination


class CustomPagination(pagination.LimitOffsetPagination):
    max_limit = 20
