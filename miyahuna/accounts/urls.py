from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginView.as_view(), name='login'),
    path('logOut',views.logOutView.as_view(),name="logout"),
    
]
