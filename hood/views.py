from django.shortcuts import render
from django.http  import HttpResponse,Http404
from django.shortcuts import render,redirect

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    neighborhoods = Neighborhood.get_all_neighborhoods()
    return render(request, 'index.html',{"neighborhoods":neighborhoods})