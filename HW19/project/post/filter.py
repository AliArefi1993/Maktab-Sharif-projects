import django_filters

from post.models import Post


class PostListFilter(django_filters.FilterSet):
    title__in = django_filters.CharFilter(
        field_name='title', lookup_expr='icontains')
    category__name = django_filters.CharFilter(lookup_expr='icontains')
    tag__name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Post
        fields = ['title', 'category', 'tag', 'published']
