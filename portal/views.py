from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required 
from .models import CustomUser , Profile, Request ,volunteer_invitations
from .forms import CustomUserCreationForm ,RequestForm ,UpdateRequestForm
from django.contrib.auth import logout as log_out
from django.urls import reverse
from django.contrib import messages
import django_filters
user_levels = {
    'l0':'SuperAdmin',
    'l2':'Manager ',
    'l3':'volunteer',
    'l4':'Normal User',
    
}
status_codes = {
    's1':'Case Resolved',
    's2':'Case Assigned to a volunteer ',
    's3':'Case under process',
    's4':'Case Open',
}  

def index(request):
    
    return render(request, 'portal/home.html')
@login_required(login_url = 'login')    
def logout(request):
    log_out(request)
    return redirect('index')

    
@login_required(login_url = 'login')       
def settings(request):
    return render(request,'portal/settings.html')
    
 
def SignUp(request):
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
                
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'portal/signup.html', {'form': form})


@login_required(login_url='login')
def req(request):
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            r = form.save(commit=False)
            r.uid = request.user
            r.save()
            form = RequestForm()
            messages.success(request, 'You have successfully submitted the request !!!')  # 
            return redirect('success')
    else:
        form = RequestForm(initial={'first_name': request.user.first_name,'last_name':  request.user.last_name})
    return render(request, 'portal/request.html', {'form': form})
def success(request):
    return render(request, 'portal/success.html',)

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
@login_required(login_url = 'login')  
def Search(request):
    if(request.user.user_type == 'l0') or (request.user.user_type == 'l2'):
        filter = UserFilter(request.GET, queryset=CustomUser.objects.all())
        people = filter.qs.order_by('first_name')
        if len(people) ==0:
            messages.warning(request, 'No results ')
        else:
            messages.success(request, 'You have {} results'.format(len(people)))
        for i in people:
            i.user_type= user_levels[str(i.user_type)]           
        return render(request, 'portal/search.html', {'filter': filter , "data" : people })  
    else:
        return render(request,'portal/unauthorized.html')
    
@login_required(login_url = 'login') 
def profile(request,user_name):

    if (request.user.user_type == 'l0') or (request.user.username == user_name):
        user_data = Profile.objects.select_related().filter(uid__username=str(user_name))
        if len(user_data)==0:
            messages.error(request, 'User doesnot exist')
            return render(request, 'portal/404.html')
                 

        else:
            return render(request, 'portal/profile.html',
                    {'data': user_data[0]})
    else:
        return render(request,'portal/unauthorized.html')

@login_required(login_url = 'login')  
def view_requests(request):
    req_data= Request.objects.select_related().filter(uid__username=str(request.user.username))
    if len(req_data)==0:
        messages.error(request, "You've not submitted any requests")
        return render(request, 'portal/blank.html')
    else:        
        for i in req_data:
            i.status= status_codes[str(i.status)]     
        return render(request, 'portal/request_view.html', {'data': req_data})

@login_required(login_url = 'login') 
def view_requests_byid(request ,request_id):   
    req_data= Request.objects.select_related().filter(id=int(request_id)).order_by('-timestamp').reverse()
    
    if len(req_data)==0:
        messages.error(request, 'This request doesnot exist')
        return render(request, 'portal/404.html')

    else:
        if (request.user.user_type == 'l0') or (request.user.username == req_data[0].uid.username):
            for i in req_data:
                i.status= status_codes[str(i.status)]  
            return render(request, 'portal/request_view_byid.html', {'data': req_data[0]})
        else:
            return render(request,'portal/unauthorized.html')
            
@login_required(login_url = 'login')     
def delete_requests_byid(request ):
    
    if request.method == "POST":
        request_id=request.POST['request_id']   
        req_data= Request.objects.select_related().filter(id=int(request_id)).order_by('-timestamp').reverse()
        if len(req_data)==0:
            messages.error(request, 'This request doesnot exist')
            return render(request, 'portal/404.html')

        else:
            if (request.user.user_type == 'l0') or (request.user.username == req_data[0].uid.username):
                req_data.delete()
                messages.success(request, 'Request deleted Successfully')
                return redirect('request_view')
            else:
                return render(request,'portal/unauthorized.html')
    
    else:
        messages.error(request, " Invalid request ")
        return render(request,'portal/blank.html',)

@login_required(login_url='login')
def update_request(request,request_id):
    req_instance=Request.objects.get(id=request_id)
    form = UpdateRequestForm(instance=req_instance)
    if request.method == "POST":
        
        req_instance=Request.objects.get(id=request_id)
        print(req)
        form = UpdateRequestForm(request.POST,instance=req_instance)
        if form.is_valid():
            r = form.save(commit=False)
            r.save()
            form = UpdateRequestForm()
            messages.success(request, 'You have successfully updated the request !!!')  # 
            return redirect('success')
    
        
        
    return render(request, 'portal/request_update.html', {'form': form ,'req_data':req_instance})
@login_required(login_url='login')
def volunteer_invite(request):
    usr=volunteer_invitations.objects.select_related().filter(uid=request.user)
    if request.method=="POST":
        if(len(usr)==0):
            inv= volunteer_invitations()
            inv.uid=request.user
            inv.save()
            messages.success(request, 'You have submitted the request for becoming a volunteer')
        else:
            messages.success(request, 'Already Submitted a request ' )
        return render(request,'portal/blank.html')
    return render (request,'portal/vol_inv.html')