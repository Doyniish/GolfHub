from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from Users import utils
from Users.models import UserData, Groups

''' This method is responsible for handling the logging of users.
 After it does that, it sends the user to their home at GolfHub. '''
def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # grab the user's groups and stats
            # {groups, stats}
            user_data = utils.main_page_load(user)
            has_groups = True
            # make sure our user has groups
            # TODO: put this code in
            # if user_data['groups'] == 'empty':
            #    has_groups = False

            # create our dictionary for our Main Page render
            context = {'has_groups': has_groups, 'user_data': user_data}
            return render(request, "MainWebsite/MainPage.html", context=context)
    else:
        return render(request, "Users/LoginScreen.html")

''' This method is responsible for handling the signing up of users. '''
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
        # TODO: Check for user errors in sign up
        return render(request, "Users/SuccessfulSignUp.html")

    else:
        return render(request, "Users/SignupScreen.html")


'''This method is responsible for handling users creating new groups. '''
def create_new_group(request):
    # Items Needed: members, creator/owner, group name

    # get our json package
    data = request.POST['json_data']
    name = data['name']
    members = data['members']
    # create our member csv string for storage
    members_str = ""
    for member in members:
        members_str += member + ","

    group = Groups(name=name, members=members_str)
