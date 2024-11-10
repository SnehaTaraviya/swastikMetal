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
        phone = request.POST.get('phone')
        company = request.POST.get('company')
        address = request.POST.get('address')
        message = request.POST.get('message')
        getintouchs = Getintouch(firstname = firstname, lastname = lastname,email = email, phone = phone, company = company,address = address,message = message)
        getintouchs.save()
        sendMailToHost(firstname,lastname,email,phone,company,address,message) 
        sendMailToCustomer(firstname,lastname,email)
        return render(request, 'thankyou.html')
    return render(request, 'getintouch.html')

def bicyclepumpparts(request):
    return render(request, 'bicycle-pump-parts.html')

def brassinsertproducts(request):
    return render(request, 'brass-insert-products.html')

def brasssensitiveolivalve(request):
    return render(request, 'brass-sensitive-oil-valves-products.html')

def brassterminal(request):
    return render(request, 'brass-terminals.html')

def brasswingnutsproducts(request):
    return render(request, 'brass-wing-nuts-products.html')

def electricalparts(request):
    return render(request, 'electrical-parts.html')

def hexnutsbolts(request):
    return render(request,  'hex-nuts-bolts.html')

def sanitaryiteams(request):
    return render(request, 'sanitary-iteams.html')

def surgicalparts(request):
    return render(request,  'surgical-parts.html')

def brassballvalve(request):
    return render(request, 'brass-ball-valve.html')

def sendMailToHost(firstname,lastname,email,phone,comapny,address,message):
    subject = "New Enquiry at Swastik Metal"
    message = f'''
    New Enquiry
    
    Name: {firstname} {lastname}
    Email: {email}
    Contact No: {phone}
    Company Name: {comapny}
    Address: {address}
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

Thank you for reaching out to Swastik Metal. We appreciate your interest in our brass products and services. Your inquiry is important to us, and our team is already reviewing your request.

We strive to respond to all inquiries promptly and will get back to you as soon as possible with the information you need. If you have any additional questions or require further assistance in the meantime, please feel free to contact us directly.

Thank you once again for considering Swastik Metal. We look forward to the opportunity to assist you.

Best regards,
Yash Taraviya, COO
Swastik Metal'''
    email_from = f'Swastik Metal<{settings.EMAIL_HOST_USER}>'
    recipient_list = [email]
    try:
        send_mail(subject, message, email_from, recipient_list)
    except Exception as e: 
        print(f"Error sending email: {e}")