from django.urls import path,include
from . import views

urlpatterns = [
   path('',views.my_student,name="my_stu"),
  
]
