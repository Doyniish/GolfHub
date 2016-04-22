from django.shortcuts import render

# Create your views here.

def home_page(request):
    # TODO: remove this when not testing
    context = {'has_groups': True}
    return render(request, "MainWebsite/MainPage.html", context)