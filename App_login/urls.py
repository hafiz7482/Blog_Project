from django.urls import path
from django.contrib.auth import views as auth_view
from . import views
from .forms import LoginForm, MyPasswordChangeForm

app_name = 'App_login'

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name = 'signup' ),
    path('login/', auth_view.LoginView.as_view(template_name='App_login/login.html', authentication_form=LoginForm), 
        name = 'login' ),
    path('logout/', auth_view.LogoutView.as_view(next_page='App_login:login'), name = 'logout' ),
    path('profile/', views.ProfileInfoView.as_view(), name = 'profile' ),
    path('address/', views.Address, name = 'address' ),
    path('address-update/<int:pk>', views.AddressUpdate.as_view(), name = 'address-update' ),
    path('password-change/', auth_view.PasswordChangeView.as_view(template_name='App_login/change_password.html', form_class=MyPasswordChangeForm, success_url='/account/passwordchangedone'), name = 'passwordchange'),
    path('passwordchangedone/', auth_view.PasswordChangeDoneView.as_view(template_name='App_login/passwordchangedone.html'),name='passwordchangedone'),
    path('add-picture/', views.add_pro_pic, name = 'add_pro_pic'),
    path('change-picture/', views.ChangeProfilePic, name = 'change_pro_pic'),

]



