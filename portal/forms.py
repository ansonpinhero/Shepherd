from django import forms
from django.forms import ModelForm ,TextInput
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser,Request

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=30,required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email','first_name','last_name')
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

class RequestForm(forms.ModelForm):
    
    class Meta:
        model =Request
        fields=('is_requesting_for_others','first_name','last_name','loc_latlong','loc_latlong_accurate','phoneno','req_description',)
        
    
class UpdateRequestForm(forms.ModelForm):
    
    class Meta:
        model =Request
        fields=('loc_latlong','loc_latlong_accurate','phoneno','req_description',)
        
      