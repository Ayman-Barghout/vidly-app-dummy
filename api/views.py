from movies.models import Movie, Genre
from rest_framework import viewsets
from .serializers import MovieSerializer, GenreSerializer

# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all().order_by('release_year')
    serializer_class = MovieSerializer

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer