from django.db.models import Q


def simple_fulltext_search(queryset, search):
    queryset = queryset.filter(
        Q(title__icontains=search) |
        Q(description__icontains=search)
    )
    return queryset
