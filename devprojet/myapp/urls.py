from django.contrib import admin
from django.urls import path
from myapp import views  
 
urlpatterns = [
    path('', views.index, name='index'),  
    path('addnew/',views.addnew, name='addnew'),  
    path('edit/<id>', views.edit, name='edit'),  
    path('update/<id>', views.update, name='update'),  
    path('delete/<id>', views.destroy, name='destroy'), 
    path('about/',views.about, name='about'), 
]