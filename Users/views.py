import json

from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from pygments.lexers import data

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
        email = request.POST['email']
        first = request.POST['first']
        last = request.POST['last']
        user = User(first_name=first, last_name=last,
                    username=username, email=email,
                    password=request.POST['password'])
        user.save()
        # create our user data entry for our user we just created
        userdata = UserData(user=user)
        userdata.save()
        # TODO: Check for user errors in sign up
        return render(request, "Users/SuccessfulSignUp.html")

    else:
        return render(request, "Users/SignupScreen.html")


def create_new_group_test(request):
    json_data = request.POST['json_data']
    data = json.loads(json_data)
    name = data["name"]
    members = "empty"
    group = Groups(name=name, members=members, owner=request.user.email)
    group.save()
    userdata = UserData.objects.get(user=request.user)
    user_group_list = userdata.groups
    user_group_list += name + ","
    userdata.save()
    res = {'success': True}

    return JsonResponse(res)

'''This method is responsible for handling users creating new groups. '''
def create_new_group(request):
    # Items Needed: members, creator/owner, group name

    # get our json package
    json_data = request.POST['json_data']
    data = json.loads(json_data)
    name = data["name"]
    members = data["members"]
    # give each member a notification that they have been requested to join this group
    if utils.set_group_notification(members, name):
        # create our member csv string for storage
        members_str = ""
        for member in members:
            members_str += member + ","

        # create our group
        group = Groups(name=name, members=members_str, owner=request.user.email)
        # save
        group.save()
        #update current user's group list
        userdata = UserData.objects.get(user=request.user)
        user_group_list = userdata.groups
        user_group_list += name + ","

        userdata.save()
        # TODO: check for errors
        # update the user with a successful creation
        res = {'success': True}
        return JsonResponse(res)
    else:
        # update the user with an unsuccessful creation
        res = {'success': False}
        return JsonResponse(res)