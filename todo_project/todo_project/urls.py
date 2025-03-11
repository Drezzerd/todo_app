from django.contrib import admin
from django.urls import path, include
from todo.views import home, run_tests
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views

def redirect_to_home(request):
    return redirect('/home/') 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redirect_to_home, name='root_redirect'),
    path('home/', home, name='home'),
    path('todo/', include('todo.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='todo/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', include('todo.urls_register')),
    path('tests/', run_tests, name='run_tests'),
]
