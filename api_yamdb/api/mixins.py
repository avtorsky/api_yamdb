from rest_framework import mixins, viewsets


class CreateListDestroyViewset(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    """Вьюсет для Create, List и Destroy."""

    serializer_class = None
    model_class = None
