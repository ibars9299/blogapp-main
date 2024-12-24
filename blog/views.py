from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'blog/index.html')
def movies(request):
    return render(request, 'blog/movies.html')
def series(request):
    return render(request, 'blog/series.html')
def books(request):
    return render(request, 'blog/books.html')
