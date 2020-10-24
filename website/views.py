import os
from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
    return render(request, 'home.html', {})

def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        #send an email
        send_mail(
            message_name, # subject
            message, # message
            message_email, # from email
            ['socialmedia.customerservice2@gmail.com'], # to email
            )

        return render(request, 'contact.html', {'message_name': message_name})

    else:
        return render(request, 'contact.html', {})

def about(request):
    return render(request, 'about.html', {})


def services(request):
    return render(request, 'service.html', {})


def pricing(request):
    return render(request, 'pricing.html', {})



def blog(request):
    return render(request, 'blog.html', {})


def blog_details(request):
    return render(request, 'blog-details.html', {})

def booking_now(request):
    return render(request, 'booking-now.html', {})

def appointment(request):
    if request.method == "POST":
        your_name = request.POST['your-name']
        your_phone = request.POST['your-phone']
        your_email = request.POST['your-email']
        your_address = request.POST['your-address']
        your_schedule = request.POST['your-schedule']
        your_day = request.POST['your-day']
        your_message = request.POST['your-message']

        #send an email
        send_mail(
            your_name + ' appointment request', # subject
            'Email:' + your_email + ' Schedule:' + your_schedule + ' Day:' + your_day + ' Message:' + your_message, # message
            your_email, # from email
            ['socialmedia.customerservice2@gmail.com'], # to email
            )

        return render(request, 'appointment.html', {
            'your_name': your_name,
            'your_phone': your_phone,
            'your_email': your_email,
            'your_address': your_address,
            'your_schedule': your_schedule,
            'your_day': your_day,
            'your_message': your_message
            })

    else:
        return render(request, 'home.html', {})
