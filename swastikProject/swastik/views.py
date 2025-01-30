from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .models import Getintouch
# Create your views here.

def home(request):
    return render(request, 'home.html')

def product(request):
    return  render(request, 'product.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def getintouch(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        message = request.POST.get('message')
        getintouchs = Getintouch(firstname = firstname, lastname = lastname,email = email,message = message)
        getintouchs.save()
        sendMailToHost(firstname,lastname,email,message) 
        sendMailToCustomer(firstname,lastname,email)
        return render(request, 'thankyou.html')
    return render(request, 'getintouch.html')

def sendMailToHost(firstname,lastname,email,message):
    subject = "New Enquiry at Swastik Metal"
    message = f'''
    New Enquiry
    
    Name: {firstname} {lastname}
    Email: {email}
    Message: {message}
    '''
    email_from = f'Swastik Metal<{settings.EMAIL_HOST_USER}>'
    recipient_list = ['iamyash226@gmail.com']
    try:
        send_mail(subject, message, email_from, recipient_list)
    except Exception as e: 
        print(f"Error sending email: {e}")


def sendMailToCustomer(firstname,lastname,email):
    subject = "Thank you for Enquiry at Swastik Metal"
    message = f'''
Hello, {firstname} {lastname}

Thank you for reaching out to Swastik Metal! We appreciate your interest and are reviewing your request. We’ll get back to you shortly—stay tuned!

Best regards,
Yash Taraviya, COO
Swastik Metal'''
    email_from = f'Swastik Metal<{settings.EMAIL_HOST_USER}>'
    recipient_list = [email]
    try:
        send_mail(subject, message, email_from, recipient_list)
    except Exception as e: 
        print(f"Error sending email: {e}")