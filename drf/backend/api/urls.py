from  django.urls import path


from . import views
 
urlpatterns = [
    path("" , views.api_home) ## empty the first params cuz we are in the api/urls where the funstion apoi_home already exist 

]