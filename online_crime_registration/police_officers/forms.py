from django import forms

from .models import Officers

from .models import RankOfOfficer

from authentication.models import Profile


class AddNewOfficersForm(forms.ModelForm):

    rank_of_officer = forms.ModelChoiceField(queryset=RankOfOfficer.objects.all(),
                                                       widget=forms.Select(attrs={
                                                      'class' :   'form-select',
                                                      'required'  :   'required'
                        }))

    class Meta :

        model = Officers

        exclude = ['profile' ,'uuid', 'active_status', 'police_officer']

        widgets = {

           
            'image'     : forms.FileInput(attrs={
                                                'class' : 'form-control',
                                                'required'  : 'required',
                                                
                                                }),
            'description'   : forms.Textarea(attrs={
                                            'class' : 'form-control',
                                            'required'  : 'required'
            })
            }
        

  
    def clean(self):

        validated_data = super().clean()

        print(  Profile.objects.values_list('username', flat=True))
        
        if validated_data.get('email') in Profile.objects.values_list('username', flat=True):

            self.add_error('email', 'email already taken')

        if validated_data.get('password') != validated_data.get('confirm_password'):

            self.add_error('confirm_password','password mismatch')

class ProfileForm(forms.ModelForm):

    class Meta:

        confirm_password    =   forms.CharField(widget=forms.PasswordInput(attrs={
                                                    'class' :   'form-control',
                                                    'required'  :   'required'
                                            }))

        model = Profile

        exclude = ['profile' ,'uuid', 'active_status']

        widgets = {

            'first_name'    :   forms.TextInput(attrs={
                                                    'class' :   'form-control',
                                                    'required'  :   'required'
                                                }),
            'last_name'    :   forms.TextInput(attrs={
                                                    'class' :   'form-control',
                                                    'required'  :   'required'
                                                }),
            'email'    :   forms.EmailInput(attrs={
                                                    'class' :   'form-control',
                                                    'required'  :   'required'
                                                }),
            'password'    :   forms.PasswordInput(attrs={
                                                    'class' :   'form-control',
                                                    'required'  :   'required'
                                                }),
           
            }
       
    def clean(self):

            validated_data = super().clean()

            print(  Profile.objects.values_list('username', flat=True))
        
            if validated_data.get('email') in Profile.objects.values_list('username', flat=True):

                self.add_error('email', 'email already taken')

            if validated_data.get('password') != validated_data.get('confirm_password'):

                self.add_error('confirm_password','password mismatch')


        


