from django.shortcuts import render
from .models import students,course
# Create your views here.

def my_student(request):
    context =  {}
    context['dataset']= students.objects.all()
    context['dataset1']= course.objects.all()

    return render(request, "show.html", context)

