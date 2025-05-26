from django import forms

from .models import User

from authentication.models import Profile

class ProfileForm(forms.ModelForm):


    class Meta:

        model = Profile

        fields = ['first_name', 'last_name', 'email', 'password','confirm_password']

        widgets = {
            'first_name'    :   forms.TextInput(attrs={
                                                            'class' :   'form-control',
                                                            'required'  : 'required'
                                                }),
            'last_name'    :   forms.TextInput(attrs={
                                                            'class' :   'form-control',
                                                            'required'  : 'required'
                                                }),                                   
            'email'    :   forms.EmailInput(attrs={
                                                            'class' :   'form-control',
                                                            'required'  : 'required'
                                                }),

            
            'password'      :   forms.PasswordInput(attrs={

                                                             'class' :   'form-control',
                                                            'required'  : 'required'
            }),
            
            #  'phone_number'    :   forms.NumberInput(attrs={
            #                                                 'class' :   'form-control',
            #                                                 'required'  : 'required'
            #                                     })
            }
        
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
                                                                
                                                    'class' :   'form-control',
                                                    'required'  :   'required'
    }))   


    def clean(self):

        validated_data = super().clean() 

        print(Profile.objects.values_list('username',flat=True))

        if validated_data.get('email') in Profile.objects.values_list('username',flat=True):

            self.add_error('email', 'email already taken!')

        if validated_data.get('password') != validated_data.get('confirm_password'):

            self.add_error('confirm_password', 'password mismatch')

        # if validated_data.get('phone_number') in Profile.objects.values_list('phone_number', flat=True):

        #     self.add_error('phone_number', 'phone number already taken!')

class UserForm(forms.ModelForm):

    class Meta:

        model = User

        exclude = ['profile', 'uuid', 'active_status','name']

        widgets ={
        'image' : forms.FileInput(attrs={
                                         'class' :   'form-control',
                                         'required'  :   'required'
        })
      
        }

        