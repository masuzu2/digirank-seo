from django.shortcuts import render
from myapp.models import Person

def index(request):
    all_Person = Person.objects.all()
    return render(request, 'index.html', {"all_person": all_Person})

def about(request):
    return render(request, 'about.html')

def contact(request):
    student_info = "6xxxxxxxxx นายสมชาย ใจดี"
    return render(request, 'contact.html', {'info': student_info})

def form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        Person.objects.create(name=name, age=age)
    return render(request, 'form.html')
