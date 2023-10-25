from django.shortcuts import render, redirect  
from myapp.froms import loginforms 
from myapp.models import login  
 
# Create your views here.  
def addnew(request):  
    if request.method == "POST":  
        form = loginforms(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('index')  
            except:  
                pass
    else:  
        form = loginforms()  
    return render(request,'addnew.html',{'form':form})  
 
def index(request):  
    employees = login.objects.all()  
    return render(request,"show.html",{'employees':employees})  
 
def edit(request, id):  
    employee = login.objects.get(id=id)  
    return render(request,'edit.html', {'employee':employee})  
 
def update(request, id):  
    employee = login.objects.get(id=id)  
    form = loginforms(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/")  
    return render(request, 'edit.html', {'employee': employee})  
     
def destroy(request, id):  
    employee = login.objects.get(id=id)  
    employee.delete()  
    return redirect("/")

def about(request):
    return render(request, "about.html")