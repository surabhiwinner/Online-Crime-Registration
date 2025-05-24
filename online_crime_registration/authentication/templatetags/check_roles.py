from django import template

register = template.Library()


def user_role_checking(request,roles):

    roles = roles.split(',')

    if request.user.is_authenticated and request.user.role  in roles:

        return True
    
    return False