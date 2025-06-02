from django.shortcuts import render, redirect


from django.views import View

from django.db import transaction

from online_crime_registration.utility import send_email

from django.contrib.auth.hashers import make_password

import threading

# Create your views here.

from .forms import ProfileForm, UserForm


class UserRegistrationView(View):

    def get(self, request, *args, **kwargs):


        profile_form = ProfileForm()

        user_form = UserForm()

        data = {
            'profile_form'  : profile_form,
            'user_form' : user_form,
            'page':'user-reg-page'
        }
        return render(request, 'user/user-registration.html',context=data)

    def post(self, request, *args, **kwargs):

        profile_form = ProfileForm(request.POST)

        user_form = UserForm(request.POST, request.FILES)

        print(profile_form.errors)

        print(user_form.errors)

        if profile_form.is_valid():

            with transaction.atomic():

                profile = profile_form.save(commit=False)

                email = profile_form.cleaned_data.get('email')

                password = profile_form.cleaned_data.get('password')

                profile.username = email

                profile.role = 'User'

                profile.password = make_password(password)

                profile.save()

                if user_form.is_valid():


                    user = user_form.save(commit=False)

                    user.profile = profile

                    user.name =f' {profile.first_name} {profile.last_name}'

                    user.save()

                    subject = 'Successfully Registered !'

                    recepient = user.profile.email

                    template = 'email/success-registration.html'

                    context = {'name': user.name, 'username':user.profile.email, 'password':password }

                    thread = threading.Thread(target=send_email,args=(subject,recepient,template,context))

                    thread.start()

                    return redirect('login')
                
            data = {
                    'profile_form'  : profile_form,
                    'user_form' : user_form,
                    'page':'user-reg-page'
                }
            return render(request, 'user/user-registration.html',context=data)
