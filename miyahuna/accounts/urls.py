from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginView.as_view(), name='login'),
    path('logOut', views.logOutView.as_view(), name="logout"),
    path('myProfile/edit', views.UpdateProfileView.as_view(), name="UpdateProfile"),
    path('myProfile/passwordChange', views.ChangePasswordView.as_view(), name="ChangePassword"),



]
