from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .models import Movie
from .permissions import IsOwnerOrReadOnly
from .serializers import MovieSerializer
from .pagination import CustomPagination
from .filters import MovieFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

class MovieAPIView(ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    pagination_class = CustomPagination
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    ordering_fields = ['-created_at']
    filterset_class = MovieFilter
