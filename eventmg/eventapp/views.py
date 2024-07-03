from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Event
from .forms import BookingForm, ContactForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def events(request):
    dict_eve = {
        'eve': Event.objects.all()
    }
    return render(request, 'events.html', dict_eve)

def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your booking is successfully completed.')
            return redirect('index')  # Replace 'index' with the name of your home page URL
   
    form = BookingForm()
    dict_form = {
        'form': form
    }
    return render(request, 'booking.html', dict_form)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for contacting us! Your message has been sent.')
            return redirect('contact')  # Redirect back to the contact page

    form = ContactForm()
    return render(request, 'contact.html')