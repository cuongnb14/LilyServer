from django.shortcuts import render

# Create your views here.
def index(request):
    data = {}
    return render(request, 'webapp/index.html', data)
