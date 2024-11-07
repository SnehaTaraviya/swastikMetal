from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def products(request):
    return  render(request, 'product.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def getintouch(request):
    return render(request, 'getintouch.html')

def bicyclepumpparts(request):
    return render(request, 'bicycle-pump-parts.html')

def brassinsertproducts(request):
    return render(request, 'brass-insert-products.html')

def brasssensitiveolivalve(request):
    return render(request, 'brass-sensitive-oli-valve.html')

def brassterminal(request):
    return render(request, 'brass-terminal.html')

def brasswingnutsproducts(request):
    return render(request, 'brass-wing-nuts-products.html')

def electricalparts(request):
    return render(request, 'electrical-parts.html')

def hexnutsbolts(request):
    return render(request,  'hex-nuts-bolts.html')

def santrairyiteams(request):
    return render(request, 'santrairy-iteams.html')

def surgicalparts(request):
    return render(request,  'surgical-parts.html')

def watermeterconnector(request):
    return render(request, 'water-meter-connector.html')