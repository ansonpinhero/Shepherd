import django_filters
from django import forms
from .models import CustomUser , Profile, Request ,volunteer_invitations


class UserFilter(django_filters.FilterSet):
    fields = ['first_name', 'last_name','username','user_type','email']

    class Meta:
        model = CustomUser
        fields = {
            'first_name' : ['contains'],
            'last_name' : ['contains'],
            'username':['exact'],
            'email':['exact'],
            'user_type':['exact'],
            
            
        }
class RequestFilter(django_filters.FilterSet):
    #fields = ['first_name', 'last_name','status','phoneno']
    uid__username = django_filters.CharFilter(label='Username')
    time_stamp = django_filters.DateFilter(field_name="timestamp", label="Date", lookup_expr='contains', widget=forms.DateInput(
            attrs={
                'id': 'datepicker',
                'type': 'date'
                
            }
        ))

    class Meta:
        model = Request
        fields = {
            'first_name' : ['contains'],
            'last_name' : ['contains'],
            'status':['exact'],
            'phoneno':['exact'],
           
            
            
        }