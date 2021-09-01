from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import Shortener
from .forms import NewUrlForm
# Create your views here.
def home(req):
    return HttpResponse("<h1>Hello! This is just checking we are working fine!</h1>")

def show(request, url):
    url_object = Shortener.objects.filter(short_url=url)
    if (len(url_object) > 0):
        url_to_find = url_object[0].long_url
        return redirect(url_to_find)
    return HttpResponse('')

def create(request):
    if request.method == 'POST':
        url = NewUrlForm(request.POST)
        if url.is_valid():
            new_url = url.save()
            return redirect('show-recent')
    else:
        form = NewUrlForm()
        context = { "form": form }
        return render(request, 'shortener/new.html', context)

def show_recent(request):
    urls = Shortener.objects.all()
    recent_url = urls[len(urls) - 1]
    context = { "url": recent_url }
    return render(request, 'shortener/index.html', context)
