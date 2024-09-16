from django.urls import path
from .views import home, redirect_to_original

urlpatterns = [
    path('', home, name='home'),
    path('<str:alias>/', redirect_to_original, name='urlpage')
]