from django import forms

from .models import CategoryChoice,StatusChoice, Crimes

from police_officers.models import Officers


class CrimesReportForm(forms.ModelForm):


    class Meta :

        model = Crimes

        # fields = '__all__'
        exclude =['uuid','active_status','police_officer']

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


    

