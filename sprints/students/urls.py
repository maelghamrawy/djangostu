from django.urls import path,include
from . import views

urlpatterns = [
   path('s/',views.my_student,name="my_stu"),
   path('c/',views.my_course,name="my_stu")
]
