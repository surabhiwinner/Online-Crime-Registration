from django import forms

from .models import CategoryChoice,StatusChoice, Crimes

from police_officers.models import Officers

from user.models import User


class CrimesReportForm(forms.ModelForm):


    class Meta :

        model = Crimes

        # fields = '__all__'
        exclude =['uuid','active_status','police_officer','status']

        widgets = {

            'title' : forms.TextInput( attrs= {
                                            'class' : 'form-control',
                                            'required' : 'required',
                                            'placeholder' : 'Enter the crime title '

                                    }),
            
            'reporting_date' : forms.DateInput( attrs= {
                                            'class' : 'form-control',
                                            'type' : 'date',
                                             'required' : 'required',
                                            
                                    }),
            
            

        }

    reporting_user = forms.ModelChoiceField(
        queryset=User.objects.all(),  # or apply filter like is_active=True
        widget=forms.Select(attrs={
            'class': 'form-control',
            'required': 'required'
        }))
    category = forms.ChoiceField(choices= CategoryChoice.choices, widget = forms.Select(
                                        attrs={

                                        'required': 'required',
                                        'class'   : 'form-control',
                                        

                                        }))
    # status = forms.ChoiceField(choices=StatusChoice.choices,widget= forms.Select( attrs = {
    #                                     'required' : 'required',
    #                                     'class' : 'form-control'
    # }))

class CrimeUpdateForm(forms.ModelForm):


    class Meta:

        
        model = Crimes

        # fields = '__all__'
        exclude =['uuid','active_status']

        widgets = {

            'title' : forms.TextInput( attrs= {
                                            'class' : 'form-control',
                                            'required' : 'required',
                                            'placeholder' : 'Enter the crime title '

                                    }),
            'reporting_user' : forms.TextInput( attrs= {
                                            'class' : 'form-control',
                                            'required' : 'required',
                                            'placeholder': 'Enter the user name'
                                            
                                    }),
            'reporting_date' : forms.DateInput( attrs= {
                                            'class' : 'form-control',
                                            'type' : 'date',
                                             'required' : 'required',
                                            
                                    }),
            
            

        }
    category = forms.ChoiceField(choices= CategoryChoice.choices, widget = forms.Select(
                                        attrs={

                                        'required': 'required',
                                        'class'   : 'form-control',
                                        

                                        }))
    status = forms.ChoiceField(choices=StatusChoice.choices,widget= forms.Select( attrs = {
                                        'required' : 'required',
                                        'class' : 'form-control'
    }))




          
    police_officer = forms.ModelChoiceField(
    queryset=Officers.objects.all(),
    widget=forms.Select(attrs={
        'class': 'form-control',
        
    })
)


    

