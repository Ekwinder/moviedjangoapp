from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required 
from django.contrib.admin.views.decorators import staff_member_required
from .models import Movie
from .forms import MovieForm
import operator
import re
from django.db.models import Q

def movie_list(request):
	movies = Movie.objects.all()
	return render(request, 'simpleapp/movie_list.html', {'movies':movies})

@login_required
def movie_detail(request, pk):
	movie = get_object_or_404(Movie, pk=pk)
	return render(request, 'simpleapp/movie_detail.html', {'movie':movie})

@staff_member_required
def movie_new(request):
	if request.method == 'POST':
		form = MovieForm(request.POST)
		if form.is_valid():
			movie = form.save(commit=False)
			movie.save()
			return redirect('simpleapp.views.movie_detail',pk=movie.pk)
	else:
		form = MovieForm()
		return render(request, 'simpleapp/movie_edit.html',{'form':form})

@staff_member_required
def movie_edit(request, pk):
	movie = get_object_or_404(Movie, pk=pk)
	if request.method == 'POST':
		form = MovieForm(request.POST, instance=movie)
		if form.is_valid():
			movie = form.save(commit=False)
			movie.save()
			return redirect('simpleapp.views.movie_detail',pk=movie.pk)
	else:
		form = MovieForm(instance=movie)
	return render(request,'simpleapp/movie_edit.html',{'form':form})

@staff_member_required
def movie_remove(request, pk):
	movie = get_object_or_404(Movie,pk=pk)
	movie.delete()
	return redirect('simpleapp.views.movie_list')

def movie_search(request):
	if request.method == 'POST':

		query = request.POST.get('q')
		
		movies = Movie.objects.all().filter(title__icontains=query)
		return render(request, 'simpleapp/movie_search.html', {'movies':movies,'query':query})

