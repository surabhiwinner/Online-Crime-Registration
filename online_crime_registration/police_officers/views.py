from django.shortcuts import render, redirect

from .models import Officers

from django.views import View

from .forms import AddNewOfficersForm


from django.contrib.auth.decorators import login_required

from django.utils.decorators import method_decorator

from authentication.permissions import permission_role

# Create your views here.


class OfficerListView(View):


    def get(self, request, *args, **kwargs):

        officers = Officers.objects.all() 

        data = {
            'page': 'officers-list-page',
            'officers' : officers        }

        return render(request, 'police_officers/officers-list.html',context= data)

@method_decorator(permission_role(roles=['Admin']), name='dispatch')
class AddNewPoliceOfficersView(View):

    def get(self, request, *args, **kwargs):

        form = AddNewOfficersForm()
        print(form.errors)
        data ={
            'form': form,
            'page': 'add-new-police-officcers-page'
        }  

        return render (request, 'police_officers/add-police-officers.html',context= data)
    
    def post(self, request,*args, **kwargs):

        print('form submitted')
        form = AddNewOfficersForm(request.POST, request.FILES)

        print(form)

        print(form.errors)

        if form.is_valid():

            form.save()

            return redirect('officers-list')
        
        data={
            'form': form,
            'page': 'add-new-police-officcers-page'
        
        }
        return render(request,'police_officers/add-police-officers.html',context= data)

