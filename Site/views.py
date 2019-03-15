from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import Site
from .forms import SiteForm

def index(request):
    Site_list = Site.objects.order_by('id')

    form = SiteForm()

    context = {'Site_list' : Site_list, 'form' : form}

    return render(request, 'Site/index.html', context)


@require_POST
def addToSite(request):
    form = SiteForm(request.POST)

    if form.is_valid():
        newToSite = Site(Title=request.POST['Title'], Year=request.POST['Year'], Rating=request.POST['Rating'])
        newToSite.save()

    return redirect('index')