from django.shortcuts import render
from django.http import HttpResponse
from employee.models import Contact
# Create your views here.


def home(request):
    query = request.GET.get('q')
    if query:
        contacts = Contact.objects.filter(
            first_name__icontains=query) | Contact.objects.filter(email__icontains=query)
    else:
        contacts = Contact.objects.all()
    return render(request, 'home.html', {'contacts': contacts})
