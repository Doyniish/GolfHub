from django.contrib.auth.models import User
from Users.models import UserData, Groups


''' This method is used to load the user data for the main page
and then return the main page with that data parsed in '''
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

    # check to see if we have groups
    if golf_group_str == 'empty':
        return golf_group_str
    else:
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
    # TODO: Create correct key list
    key_list = ['stat1', 'stat2', 'stat3', 'stat4']
    # create our stats dictionary
    stats_dic = {}
    # check to see if they have stats saved
    if user.stats == 'empty':
        return 'empty'
    else:
        # grab our user's stat string out of the database
        users_stats_list = user.stats.split(',')
        i = 0
        # loop over our user stat string
        for stat in users_stats_list:
            stats_dic.update({key_list[i]: stat})
            # move to next key
            i += 1
        return stats_dic


''' This method is used to set the notification for each user requested
to join a group by another user '''
def set_group_notification(user_email_list, group_name):
    # user list is a of the users' emails
    user_list = []
    # get each user and then add it to the list
    for user_email in user_email_list:
        user_list.append(User.objects.get(email=user_email))

    # update each userdata object with the notification
    for user in user_list:
        userdata = UserData.objects.get(user=user)
        userdata.has_invite = True
        userdata.invite_type = False
        #TODO: Might need to add group_id to this list,
        # TODO: to find the group after they accept the invite
        userdata.invite_name = group_name
        userdata.save()
    # TODO: Check for errors
    return True

    # TODO: Send the user an email