from rest_framework import pagination
from rest_framework.views import Response


class CustomPageNumberPagination(pagination.PageNumberPagination):
    page_size = 15
    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'results': data
        })


class CustomLimitOffsetPagination(pagination.LimitOffsetPagination):
    default_limit = 10
    max_limit = 15