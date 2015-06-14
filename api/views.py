from rest_framework import status
from rest_framework.decorators import permission_classes, authentication_classes, api_view
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from simpleapp.models import Movie
from api.serializers import MovieSerializer
from rest_framework.views import APIView
from rest_framework import filters
from rest_framework import generics

@api_view(['GET'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
def movie_list(request):
    """
    List all movies.
    """
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)


@api_view(['POST'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAdminUser,))
def movie_add(request):
	if request.method == 'POST':
	    serializer = MovieSerializer(data=request.DATA)
	    if serializer.is_valid():
	        serializer.save()
	        return Response(serializer.data, status=status.HTTP_201_CREATED)
	    else:
	        return Response(
	            serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAdminUser,))
def movie_detail(request, pk):
    """
    Get, udpate, or delete a specific movie
    """
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MovieSerializer(movie, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['POST'])
# def movie_search(request):
# 	query = kwargs['q']
# 	movies = Movie.objects.all().filter(title__icontains=query)
# 	serializer = MovieSerializer(movies, many=True)
# 	return Response(serializer.data)

class MovieSearch(generics.ListAPIView):
	model = Movie
	serializer_class = MovieSerializer

	def get_queryset(self):
		"""
		Optionally restricts the returned purchases to a given user,
		by filtering against a `username` query parameter in the URL.
		"""
		queryset = Movie.objects.all()
		title = self.request.query_params.get('title', None)
		if title is not None:
			queryset = queryset.filter(title__icontains=title)

		return queryset


