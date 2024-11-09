from django.urls import path
from swastik import views

urlpatterns = [
    path("",views.home,name="Home"),
    path("home", views.home, name="Home"),
    path("product", views.product,name="Products"),
    path("aboutus", views.aboutus, name="AboutUs"),
    path("getintouch", views.getintouch, name="GetinTouch"),
    path("bicyclepumpparts",views.bicyclepumpparts, name="BicyclePumpParts"),
    path("brassinsertproducts",views.brassinsertproducts, name="BrassInsertProducts"),
    path("brasssensitiveolivalve", views.brasssensitiveolivalve, name="BrassSensitiveOliValve"),
    path("brassterminal", views.brassterminal, name="BrassTerminal"),
    path("brasswingnutsproducts",views.brasswingnutsproducts, name="BrassWingNutsProducts"),
    path("electricalparts", views.electricalparts, name="ElectricalParts"),
    path("hexnutsbolts", views.hexnutsbolts, name="HexNutsBolts"),
    path("surgicalparts", views.surgicalparts, name="SurgicalParts"),
    path("brassballvalve", views.brassballvalve, name="BrassBallValve"),
    path("sanitaryiteams", views.sanitaryiteams, name="SanitaryIteams"),
]
