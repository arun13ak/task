
from django.urls import path,include
from task import views

urlpatterns = [
    path('',views.home,name= 'home'),
    path('prompt/',views.prompt,name= 'prompt'),
]