import django_filters

from post.models import Post


class PostListFilter(django_filters.FilterSet):
    # creator_isnull = django_filters.BoleanFilter(field_name='creator', lookup_expr='isnull')
    title__in = django_filters.CharFilter(
        field_name='title', lookup_expr='icontains')

    class Meta:
        model = Post
        fields = ['title']
