


'''This method is used to load the user data for the main page
and then return the main page with that data parsed in'''
from django.contrib.auth.models import User

from Users.models import UserData, Groups


def main_page_load(user):
    groups = get_user_golf_groups(user)
    stats = get_user_stats(user)
    return {'groups': groups, 'stats': stats}


''' This method returns the groups the user is apart of '''
def get_user_golf_groups(user):
    # get our user's data object
    userdata = UserData.objects.get(user=user)
    # each group is separated by commas
    golf_group_str = userdata.golf_groups
    # get each golf group object
    group_list = golf_group_str.split(',')
    # get each user in each of the golf groups
    # create a key value pair, key: group name, value: users of the group
    master_list = {}
    for group_str in group_list:
        group = Groups.objects.get(name=group_str)
        # get each user object of that group
        group_users_list = group.members.split(',')
        user_objects = []
        # users are saved by email
        for user_str in group_users_list:
            user_objects.append(User.objects.get(email=user_str))

        #add key and user list to create a group
        master_list.update({group_str: user_objects})
        # TODO: add the the owner of the group to the list
    # return the master list with all the groups and users in each group
    return master_list

''' This method returns the stats of the current user '''
def get_user_stats(user):
    pass