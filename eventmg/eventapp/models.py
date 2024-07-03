from django.db import models

class Event(models.Model):
    img = models.ImageField(upload_to="picture")
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Booking(models.Model):
    cust_name = models.CharField(max_length=50)
    cust_phn = models.CharField(max_length=12)
    name = models.ForeignKey(Event, on_delete=models.CASCADE)
    booking_date = models.DateField()
    booked_on = models.DateField(auto_now=True)

    def __str__(self):
        return f"Booking for {self.name} by {self.cust_name}"

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
