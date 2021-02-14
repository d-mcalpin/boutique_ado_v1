from django.shortcuts import render

# Create your views here.


def index(request):
    """ A View to Return the Index Page """
    return render(request, 'home/index.html')
