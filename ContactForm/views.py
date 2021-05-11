from django.shortcuts import render, HttpResponseRedirect

from .models import ContactModel

from .forms import ContactModelForm

def contact(request):
    return render(request, 'ContactForm/contact.html')

def contact(request):
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = ContactModelForm()
    return render(request, "ContactForm/contact.html", {'form': form})

