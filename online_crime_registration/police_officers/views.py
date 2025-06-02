from django.shortcuts import render, redirect

from .models import Officers

from django.views import View

from .forms import AddNewOfficersForm

import threading 

from online_crime_registration.utility import send_email

from django.db import transaction

from django.contrib.auth.hashers import make_password

from django.contrib.auth.decorators import login_required

from django.utils.decorators import method_decorator

from authentication.permissions import permission_role

from user.forms import ProfileForm

# Create your views here.


class OfficerListView(View):


    def get(self, request, *args, **kwargs):

        officers = Officers.objects.all() 

        data = {
            'page': 'officers-list-page',
            'officers' : officers        }

        return render(request, 'police_officers/officers-list.html',context= data)

# @method_decorator(permission_role(roles=['Admin']), name='dispatch')
# class AddNewPoliceOfficersView(View):

#     def get(self, request, *args, **kwargs):

#         officer_form = AddNewOfficersForm()
#         profile_form = ProfileForm()
#         print(officer_form.errors)
#         print(profile_form.errors)
#         data ={
#             'officer_form': officer_form,
#             'profile_form' : profile_form,
#             'page': 'add-new-police-officcers-page'
#         }  

#         return render (request, 'police_officers/add-police-officers.html',context= data)
    
#     def post(self, request,*args, **kwargs):

#         print('form submitted')

#         profile_form = ProfileForm(request.POST)

#         officer_form = AddNewOfficersForm(request.POST, request.FILES)

#         print(officer_form.errors)

#         print(profile_form.errors)

#         if form.is_valid():

#             form.save()

#             return redirect('officers-list')
        
#         data={
#             'form': form,
#             'page': 'add-new-police-officcers-page'
        
#         }
#         return render(request,'police_officers/add-police-officers.html',context= data)

@method_decorator(permission_role(roles=['Admin']), name='dispatch')
class OfficerRegistrationView(View):

    def get(self,request,*args,**kwargs):

        profile_form = ProfileForm()

        officer_form = AddNewOfficersForm()

        data = {
            'profile_form'  : profile_form,
            'officer_form'  : officer_form
        }

        return render(request,'police_officers/add-police-officers.html',context=data)

    def post(self, request, *args , **kwargs):

        profile_form = ProfileForm(request.POST)   
    
        officer_form = AddNewOfficersForm(request.POST,request.FILES)

        print(profile_form.errors)

        print(officer_form.errors)

        if profile_form.is_valid():

            with transaction.atomic():

                profile = profile_form.save(commit=False)

                email = profile_form.cleaned_data.get('email')

                password = profile_form.cleaned_data.get('password')

                profile.username = email

                profile.role = 'Officer'

                profile.password = make_password(password)

                profile.save()

                if officer_form.is_valid():


                    officer = officer_form.save(commit=False)

                    officer.profile = profile

                    officer.police_officer = f' {profile.first_name} {profile.last_name}'

                    officer.save()

                    subject = 'Successfully Registered !!!'

                    recepient = officer.profile.email
                    
                    template = 'email/success-registration.html'

                    context = {'police_officer':officer.police_officer,'username':officer.profile.email,'password':password}

                    thread = threading.Thread(target=send_email,args=(subject,recepient,template,context))

                    thread.start()

                    return redirect('officers-list')
                
        data = {
            'profile_form'  : profile_form,
            'officer_form'  : officer_form
        }

        return render(request,'police_officers/add-police-officers.html',context=data)
