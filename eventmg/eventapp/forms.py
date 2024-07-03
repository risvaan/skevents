from django import forms
from .models import Booking, Contact

class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__' 

        widgets = {
            'booking_date': DateInput(),  
        }

        labels = {
            'cust_name': "Customer Name",  
            'cust_phn': "Customer Phone",
            'name': "Event Name",
            'booking_date': "Booking Date",
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']