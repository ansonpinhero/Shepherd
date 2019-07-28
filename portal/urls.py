"""shepherd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth import views as auth_views
from django.urls import path,include
from . import views
from django.conf.urls.static import static
urlpatterns = [
    
    path('',views.index,name='index'),
    path('dashboard',views.index,name='dashboard'),
    path('accounts/login/',auth_views.LoginView.as_view(template_name='portal/login.html'),name='login'),
    path('accounts/logout', views.logout,name='logout'),
    path('accounts/signup/', views.SignUp, name='signup'),
    path('settings/',views.settings,name='settings'),
    path('request/new/',views.req,name='request_form'),
    path('request/view/',views.view_requests,name='request_view'),
    path('request/view/<int:request_id>/',views.view_requests_byid,name='request_view_byid'),
    path('request/delete/',views.delete_requests_byid,name='request_delete_byid'),
    path('request/update/<int:request_id>/',views.update_request,name='request_update_byid'),
    path('success/',views.success,name='success'),
    path('search/users/',views.Search,name='search_users'),
    path('search/requests/',views.RequestSearch,name='search_requests'),
    path('user/<str:user_name>/',views.profile,name='user_profile'),
    path('user/<str:user_name>/requests/',views.view_requests_by_user,name='requests_by_user'),
    path('invite/volunteer',views.volunteer_invite,name='volunteer_invite')
     
    
]
handler404 = 'portal.views.view_404'