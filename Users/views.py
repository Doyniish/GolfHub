from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from Users.models import UserData


def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return main_page_load(user)
    else:
        return render(request, "Users/LoginScreen.html")

def signup_page(request):
    if request.method == 'POST':
        # create our user
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        first = request.POST['first']
        last = request.POST['last']
        user = User(first_name=first, last_name=last,
                    username=username, email=email,
                    password=password)
        user.save()
        # create our user data entry for our user we just created
        userdata = UserData(user=user)
        userdata.save()

    else:
        return render(request, "Users/SignupScreen.html")
