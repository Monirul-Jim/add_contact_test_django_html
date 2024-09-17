from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm


def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'employee/contact_form.html', {'form': form})


def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'employee/contact_detail.html', {'contact': contact})


def edit_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'employee/contact_form.html', {'form': form})


def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('home')
    return render(request, 'employee/contact_confirm_delete.html', {'contact': contact})
