from django.contrib.auth.models import User
from Users.models import UserData, Groups, UserStats, Requests

###########################
# Data Retrieving Methods #
###########################


''' This method is used to load the user data for the main page
and then return the main page with that data parsed in '''
def main_page_load(user):
    groups = get_user_golf_groups(user)
    stats = get_user_stats(user)
    return {'groups': groups, 'stats': stats}


''' This method returns the groups the user is apart of '''
def get_user_golf_groups(user):
    # get our user's data object #
    user_data = UserData.objects.get(user=user)
    # get our groups that the user is apart of #
    return user_data.groups.all()

''' This method returns the users of a particular group '''
def get_group_users(group):
    return group.members.all()

''' This method returns a user's stats object '''
def get_user_stats(user):
    user_data = UserData(user=user)
    return user_data.stats


###################
# Request Methods #
###################


# Send Request #


def send_request(type, list, name, id):
    if type == 'group':
        return group_request(list, name, id)
    elif type == 'event':
        return event_request(list, name, id)

''' This method is used to send every user in the list a request to join a
    certain group '''
def group_request(list, name, id):
    # list: [user object]
    for member in list:
        # create a new request for each member
        request = Requests(invite_type=False,
                           invite_object_id=id,
                           invite_name = name)
        request.save()
        user_data = UserData.objects.get(user=member)
        user_data.requests.add(request)

    # TODO: Check for errors
    return 'success'

def event_request(list, name, request):
    pass


# Accept Request #


def accept_request(type, user, request):
    if type == 'group':
        return accept_group_request(user, request)
    elif type == 'event':
        return accept_event_request(user, request)

def accept_group_request(user, request):
    # add user to the group
    group = Groups.objects.get(id=request.id)
    group.members.add(user)
    group.save()
    # remove request
    user_data = UserData.objects.get(user=user)
    user_data.requests.remove(request)
    # add group to user's groups
    user_data.groups.add(group)
    user_data.save()

def accept_event_request(user, request):
    pass

####################
# Creating Methods #
####################


''' This method is used when creating a new user in Users/views/sign_up()'''
def create_new_user(data):
    # data is the user that they have entered when signing up

    # start by creating the new user object
    user = User(email=data['email'],
                username=data['username'],
                password=data['password'],
                first_name=data['first_name'],
                last_name=data['last_name'])
    user.save()
    #now let's create the new user data object, where all of golf hub data is stored
    user_data = UserData()
    user_data.user = user
    # create our stats object for the userdata object
    user_stats = UserStats()
    user_stats.save()
    # assign it to the user data object
    user_data.stats = user_stats
    user_data.save()
    # TODO: check for errors
    # return success
    return {'status':'success'}

''' This method is used when creating a new group in User/views/create_new_group()'''
def create_new_group(json_data, user):
    # json data is sent from client side with keys: ['name':string, 'members':[emails]]
    name = json_data['name']
    member_list = json_data['members']
    user_list = []
    # loop through the list of emails to get each user object
    for member_email in member_list:
        user_list.append(User.objects.get(email=member_email))

    # create the empty group
    group = Groups(name=name, owner=user)
    group.save()

    # send each a notification that they have been requested to this group
    send_request('group', user_list, name, group.id)
    return {'status':'success'}
