from django.urls import path
from swastik import views

urlpatterns = [
    path("",views.home,name="Home"),
    path("home", views.home, name="Home"),
    path("product", views.product,name="Products"),
    path("aboutus", views.aboutus, name="AboutUs"),
    path("getintouch", views.getintouch, name="GetinTouch"),
]
