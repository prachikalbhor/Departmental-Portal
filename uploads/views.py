from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import REGISTER, LOGIN_DETAILS, FILES1, TEMP_FILES
# Create your views here.

info = {}

def login(request):
    global info
    if request.method=="POST":
        data = request.POST
        em_id = data['email_id']
        ps = data['password']
        obj = REGISTER.objects.filter(email_id=em_id,password=ps)
        id = len(obj)
        if (id>0):
            request.session["login"] = True
            request.session['u_id'] = obj[0].user_id
            request.session['u_name'] = obj[0].name
            request.session['u_email'] = obj[0].email_id
            request.session['u_password'] = obj[0].password
            print(request.session)
            l = LOGIN_DETAILS(email_id=data['email_id'],password=data['password'])
            l.save()
            if(request.session['u_email']==em_id and request.session['u_password']==ps):
                info = {'user_id':request.session['u_id'],'name':request.session['u_name'],'email_id':request.session['u_email'],'password':request.session['u_password']}
                return redirect("/file/")
    return render(request,"home.html")

def logout(request):
    global info
    info = {}
    request.session["name"] = False
    request.session["login"] = False
    return redirect('/home/')

def index(request):
    global info
    L = []
    context = {}
    if(len(info)>0):
        temp = info['name']
        L = temp.split(" ")
        temp1 = L[0]
        context={'name':temp1}
    return render(request,"home.html",context)



def register(request):
    context = {}
    if request.method=='POST':
        print("in register")
        data=request.POST
        r=REGISTER(name=data["name"], email_id=data["email_id"], department_name=data["department_name"], password=data["password"])
        r.save()
        context = {'display':"Registered Successfully"}

    return render(request,"register.html",context)

def upload(request):
    context = {}
    if request.method=="POST":
        data = request.POST
        pic = request.FILES['image']
        r = TEMP_FILES(title=data['title'],description=data['description'],image=pic)
        r.save()
        print(pic)
        context = {'display':"File Uploaded Successfully"}
    return render(request,"upload.html",context)


def files(request):
    global info
    context = {}
    temp = ""
    L = []
    r = TEMP_FILES.objects.all()
    if(len(info)>0):
        temp = info['name']
        L = temp.split(" ")
        temp = L[0]
    context = {'allfiles':r,'name':temp}
    return render(request,"file.html",context)

def delete1(request,file_id):
    f = file_id
    print(f)
    obj = TEMP_FILES.objects.get(pk=f)
    obj.delete()
    return redirect("/file/")