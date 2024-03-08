from django.shortcuts import render,redirect
from . models import regtable

# Create your views here.
def welcome(request):
    return render(request,"welcome.html")
def Reg(request):
    if request.method=="POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        gen=request.POST.get('Gender')
        adr=request.POST.get('Address')
        mb=request.POST.get('Number')
        pin=request.POST.get('pin')
        uname=request.POST.get('Username')
        pswd=request.POST.get('Password')
        obj = regtable.objects.create(Fname=fname,Lname=lname,Gender=gen,Adrs=adr,Mobnum=mb,Pin=pin,Username=uname,Password=pswd)
        obj.save()
        if obj:
            s = "Successfully Registered"
            return render(request,"reg.html",{"success":s})
        else:
            s = "Not registered" 
            return render(request,"reg.html",{"success":s}) 
    else:
        return render(request,"Reg.html")
        

def Login(request):
    if request.method=="POST":
        user=request.POST.get('Username')
        pssw=request.POST.get('Password')
        obj=regtable.objects.filter(Username=user,Password=pssw)
        if obj:
            request.session['user']=user
            request.session['pssw']=pssw
            return render(request,"welcome.html")
        else:
            request.session['user']=""
            request.session['pssw']=""
            return render(request,"Login.html",{"msg":"check you data"})
    else:
        return render(request,"Login.html")

def details(request):
    obj=regtable.objects.all
    return render(request,"details.html",{"data":obj})

def delete(request):
    idno=request.GET.get("idno")
    regobj=regtable.objects.get(id=idno)
    if regobj:
        regobj.delete()
        return redirect("/")

        