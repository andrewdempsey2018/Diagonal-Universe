from django.shortcuts import render, HttpResponseRedirect

from django.urls import reverse

from post import views

from .models import ContactModel

from .forms import ContactModelForm

def contact(request):
    return render(request, 'ContactForm/contact.html')

def contact(request):
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(views.view_post))
    else:
        form = ContactModelForm()
    return render(request, "ContactForm/contact.html", {'form': form})

