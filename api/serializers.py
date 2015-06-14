from rest_framework import serializers
from simpleapp.models import Movie

class MovieSerializer(serializers.ModelSerializer):
	class Meta:
		model = Movie
		fields = ('id','title','desc','rating')