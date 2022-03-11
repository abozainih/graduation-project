from django.urls import path, include
from . import views
from .api import urls

urlpatterns = [
    path('list/', views.customersListView.as_view(), name='CustomersList'),
    path('api/', include(urls)),

]