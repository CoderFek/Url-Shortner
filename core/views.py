from django.shortcuts import render, redirect, get_object_or_404
from .forms import URLform
from .models import URL
# Create your views here.

def home(request):
    form = URLform(request.POST or None)
    if form.is_valid():
        url = form.save()
        short_url = request.build_absolute_uri('/') + url.alias
        return render(request, 'core/success.html', {'short_url':short_url})
    return render(request, 'core/home.html', {'form':form})

def redirect_to_original(request, alias):
    url = get_object_or_404(URL, alias=alias)
    return redirect(url.original_url)