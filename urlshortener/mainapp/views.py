from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import Shortener
from .forms import NewUrlForm
from .helpers import generate_url
# Create your views here.
def home(req):
    return HttpResponse("<h1>Hello! This is just checking we are working fine!</h1>")

def show(request, url):
    url_object = Shortener.objects.filter(short_url=url)
    url_to_find = url_object[0].long_url
    return redirect(url_to_find)

def create(request):
    if request.method == 'POST':
        url = NewUrlForm(request.POST)
        if url.is_valid():
            new_url = url.save()
            return redirect('show-all')
    else:
        form = NewUrlForm()
        context = { "form": form }
        return render(request, 'shortener/new.html', context)

def show_all(request):
    urls = Shortener.objects.all()
    context = { "urls": urls }
    return render(request, 'shortener/index.html', context)
