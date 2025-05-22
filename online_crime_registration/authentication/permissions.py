from django.shortcuts import redirect


def permission_role(roles):

    def decorator(func):

        def wrapper(request, *args, **kwargs):

            if request.user.is_authenticated and request.user.role in roles:

                return func(request,*args,**kwargs)
            
            return redirect('login')
        return wrapper
    
    return decorator