from django.shortcuts import render,redirect

from .models import Crimes

from police_officers.models import Officers

from django.views import View

from django.db.models import Q

from .forms import CrimesReportForm, CrimeUpdateForm

from django.contrib.auth.decorators import login_required

from django.utils.decorators import method_decorator

from authentication.permissions import permission_role

from authentication.models import Profile

from user.models import User


# Create your views here.

class CrimesListView(View):

    def get(self, request , *args , **kwargs):


        # uuid = kwargs.get('uuid')
        # officer = Officers.objects.get(uuid)
        crimes = Crimes.objects.all()

        

        

        # if request.user.role == 'Officer':
        # if hasattr(request.user, 'role'):
        role =getattr(request.user, 'role')

        if  role == 'Officer':
            crimes = Crimes.objects.filter(police_officer__profile = request.user)
        elif  role =='User':  
            user = User.objects.get(profile = request.user)
            crimes = Crimes.objects.filter(reporting_user = user)
        elif role == 'Admin':

            crimes = Crimes.objects.all()

        # for crime in crimes:
        #     print(crime.reporting_user)
     
        print(request.user)

        # profile = Profile.objects.all()
        # profile = officer.police_officer

        # is_owner = request.user
        print(crimes)
        data = {
            'crimes' : crimes,
            'page'   : 'crime-list',
           
            
        }

        return render(request,'crimes/crime-list.html', context=data)
class HomeView(View):

    def get(self, request, *args, **kwargs):

        data = {
            'page' : 'home-page'    }

        return render(request , 'crimes/home.html',context=data) 

class AboutView(View):

      def get(self, request, *args, **kwargs):

        data = {
            'page' : 'about-page'    }

        return render(request , 'crimes/about.html',context=data) 
      
class ContactView(View):

      def get(self, request, *args, **kwargs):

        data = {
            'page' : 'contact-page'    }

        return render(request , 'crimes/contact.html',context=data) 
      

@method_decorator(permission_role(roles=['Officer','User']),name='dispatch')
class ReportCrimeView(View):


    def get(self, request, *args , **kwargs):

        # data ={
        #     'page' : 'report-crime-page'
        # }

        form = CrimesReportForm()
        user = User.objects.get(profile = request.user)

        data ={
            'form' : form,
            'user' : user,
            'page' : 'report-crime-page'
        }

        return render(request,'crimes/report_crime.html', context=data)
    
    def post(self, request, *args , **kwargs):

        if request.method == 'POST':
            form = CrimesReportForm(request.POST)
            user = User.objects.get(profile = request.user)
            # print(form)
            print(form.errors)

            if form.is_valid():

                crime = form.save(commit=False)

                crime.reporting_user = user

                form.save()

                return redirect('crimes')
        
            data = {
             'form' : form
            }

            return render(request,'crimes/report_crime.html', context=data)

@method_decorator(permission_role(roles=['Admin','Officer']),name='dispatch')
class CrimeUpdateView(View):

    def get(self, request, *args , **kwargs):

        uuid = kwargs.get('uuid')

        crime = Crimes.objects.get(uuid=uuid)

        role = request.user.role

        if role == 'Officer':
            officers = Officers.objects.filter(profile = request.user)
            
        elif role == 'Admin':
            officers =Officers.objects.all()

        form = CrimeUpdateForm(instance=crime)

        form.fields['police_officer'].queryset = officers
        print(officers)
        print(form)
        data = {
            'form' : form,
            'officers': officers
        }

        return render(request, 'crimes/update-crime.html', context=data)
    
    def post(self, request, *args, **kwargs):

        uuid = kwargs.get('uuid')

        crime = Crimes.objects.get(uuid=uuid)

        print(crime)

        # form = CrimesReportForm(request.POST , instance= crime)

        form = CrimeUpdateForm(request.POST, instance= crime)

        if form.is_valid():

            form.save()

            return redirect('crimes')


@method_decorator(permission_role(roles=['Admin', 'Officer']),name='dispatch')
class CrimeDeleteView(View):

        def get (self, request, *args, **kwargs):

            uuid = kwargs.get('uuid')

            crime = Crimes.objects.get(uuid = uuid)

            crime.delete()
            print(crime)

            return redirect('crimes')

@method_decorator(permission_role(roles=['Admin','Officer','User']),name='dispatch')
class  CrimeDetailsView(View):

        def get(self, request, *args, **kwargs):

            uuid = kwargs.get('uuid')

            crime = Crimes.objects.get(uuid=uuid)

            data = {
                'crime' : crime
            }

            return render(request,'crimes/crime-details.html', context=data)