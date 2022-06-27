from rest_framework import filters, mixins, viewsets, pagination

from reviews.models import Genre, Category, Title
from .serializers import GenreSerializer, CategorySerializer, TitleSerializer, TitleReadonlySerializer
from .pagination import TitleGenreCategoryPagination


class GenreViewSet(mixins. CreateModelMixin,
                   mixins.ListModelMixin, 
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    """"Вью-класс для жанров"""
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    pagination_class = pagination.PageNumberPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',) 


class CategoryViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin, 
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    """Вью-класс для категорий"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = pagination.PageNumberPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',) 


class TitleViewSet (viewsets.ModelViewSet):
    """"Вью-класс для произведений"""
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    http_method_names = ['get', 'post', 'patch', 'delete', 'head']
    # Убираем метод put из разрешенных
    pagination_class = TitleGenreCategoryPagination

    def get_serializer_class(self):
        if self.action in ('retrieve', 'list'):
            return TitleReadonlySerializer
        return TitleSerializer
        # используем разные сериализаторы в зависимости от метода

    
    def get_queryset(self):
        queryset = Title.objects.all()
        category = self.request.query_params.get('category')
        genre = self.request.query_params.get('genre')
        name = self.request.query_params.get('name')
        year = self.request.query_params.get('year')
        if genre is not None:
            queryset = queryset.filter(genre__slug=genre)
        if category is not None:
            queryset = queryset.filter(category__slug=category)
        if name is not None:
            queryset = queryset.filter(name=name)
        if year is not None:
            queryset = queryset.filter(year=year)
        return queryset
        # устанавливаем фильтрацию по полям
        # Если в запросе присутствуют ключи фильтруемых полей
        # фильтруем queryset по содержимому полей
