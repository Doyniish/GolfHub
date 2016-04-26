from django.shortcuts import render, redirect


# Create your views here.

def home_page(request):
    # TODO: remove this when not testing
    context = {'has_groups': True}
    if request.user.is_authenticated:
        return render(request, "MainWebsite/MainPage.html", context)
    else:
        return redirect("/user/login/")