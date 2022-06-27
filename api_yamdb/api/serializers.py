from rest_framework import serializers

from reviews.models import Category, Genre, Title

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'slug')
        model = Genre


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'slug')
        model = Category


class TitleReadonlySerializer (serializers.ModelSerializer):
    """"Сериализатор произведений для List и Retrieve"""
    category = CategorySerializer(read_only=True)
    genre = GenreSerializer(read_only=True, many=True) 
        
    class Meta:
        fields = ('id', 'name', 'year', 'rating', 'description', 'genre', 'category')
        # прямо прописываем поля, для порядка выдачи в JSON
        model = Title

class TitleSerializer(serializers.ModelSerializer):
    """Сериализатор произведений для Create, Partial_Update и Delete"""
    category = serializers.SlugRelatedField(slug_field='slug', queryset=Category.objects.all())
    genre = serializers.SlugRelatedField(slug_field='slug', queryset = Genre.objects.all(), many=True)
    # Many=True, потому что ManytoManyField

    class Meta:
        fields = ('__all__')
        model = Title