from django.shortcuts import render
from .models import students,course
# Create your views here.

def my_student(request):
    context =  {}
    context['dataset']= students.objects.all()
    return render(request, "show.html", context)

def my_course(request):
    contexts = {}
    contexts['dataset']= course.objects.all()
    return render(request, "show.html", contexts)