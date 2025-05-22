from django.shortcuts import render,redirect


from django.contrib.auth import authenticate, login,logout

from django.views import View

from .forms import LoginForm

# Create your views here.

class LoginView(View):

    def get(self, request, *args, **kwargs):

        form = LoginForm()

        data = {
            'page': 'login-page',
            'form' : form 
        }

        return render(request, 'authentication/login.html', context= data)
    
    def post(self, request , *args ,**kwargs):

        form = LoginForm(request.POST)

        error = None

        if form.is_valid():

            username = form.cleaned_data.get('username')

            password = form.cleaned_data.get('password')

            print(username,password)

            user = authenticate(username=username,password=password)

            if user:

                login(request, user)

                return redirect('officers-list')
            
            error ='Invalid credencials'


        data = {
            'form': form,
            'error': error,
            'page': 'login-page'
        }
        return render(request, 'authentication/login.html', context=data)
    
class LogoutView(View):

    def get(self, request, *args, **kwargs):

        logout(request)

        return redirect('crimes')
 

