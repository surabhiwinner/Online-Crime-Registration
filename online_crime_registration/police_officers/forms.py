from django import forms

from .models import Officers


class AddNewOfficersForm(forms.ModelForm):

    class Meta :

        model = Officers

        exclude = ['uuid', 'active_status']

        widgets = {

            'police_officer' : forms.TextInput(attrs={
                                                    'class' :   'form-control',
                                                    'required'  :   'required',
                                                    'placeholder'   : 'Enter the name of police officer '
                                                   
                                                }),

            'image'     : forms.FileInput(attrs={
                                                'class' : 'form-control',
                                                'required'  : 'required',
                                                
                                                }),
            'description'   :   forms.Textarea(attrs={
                                                    'class' : 'form-control',
                                                    'required': 'required',
                                                    'placeholder': "Enter the officer's profile"
            })


        }


