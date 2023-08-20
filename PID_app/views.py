from django.shortcuts import render
import json
from django.core import serializers
from .models import *
from django.http import HttpResponse, JsonResponse
from django.db.models import Q
from django.db.models import Count
from django.views.decorators.cache import never_cache
from django.core.files.storage import FileSystemStorage
from datetime import datetime
from .models import*
from django.views.decorators.csrf import ensure_csrf_cookie
from Detectgarbage import detect1
# Create your views here.
###############LOGIN START

# Create your views here.
def Home_page(request):
    return render(request,'index.html',{})

def Reg_customer(request):
    return render(request,'Reg_customer.html',{})



def Save_cutomer(request):
    name=request.GET.get("name")
    place=request.GET.get("place")
    phone=request.GET.get("phone")
    uname=request.GET.get("uname")
    pswrd=request.GET.get("pswrd")

    
    print(name+place+phone+uname+pswrd)
  
    data={}
    try:
        ob1=Customer_reg(Name=name,Address=place,Phone=phone,Username=uname,Password=pswrd)

    



        ob1.save()
        usid=ob1.id
        request.session['usid']=usid
        request.session['utype']='customer'
        data["result"]="yes"
    except Exception as e:
        print(e)
        data["result"]="no"
    print (data)
    return JsonResponse(data,safe=False)


def Reg_Volunteer(request):
    return render(request,'Reg_volunteer.html',{})











def Save_volunteer(request):
    name=request.GET.get("name")
    place=request.GET.get("place")
    phone=request.GET.get("phone")
    uname=request.GET.get("uname")
    pswrd=request.GET.get("pswrd")
    
    print(name+place+phone+uname+pswrd)
  
    data={}
    try:
        ob1=Volunteer_reg(Name=name,Address=place,Phone=phone,Username=uname,Password=pswrd)
        ob1.save()


        data["result"]="yes"
    except Exception as e:
        print(e)
        data["result"]="no"
    print (data)
    return JsonResponse(data,safe=False)








def Login_page(request):
    return render(request,'Signin.html',{})




def CheckLogin(request):
    uname=request.GET.get("uname")
    pswrd=request.GET.get("pswrd")
    utype=request.GET.get("utype")
    print(uname,pswrd,utype)
    if(utype=='Volunteer'):
        try:
            ob=Volunteer_reg.objects.get(Username=uname,Password=pswrd)
            
            request.session["uname"]=uname
            data={"status":"Volunteer"}
            return JsonResponse(data,safe=False)
        except:
            data={"status":0}
            return JsonResponse(data,safe=False)
    elif(utype=='Customer'):
        print("Customer")
        try:
            ob=Customer_reg.objects.get(Username=uname,Password=pswrd)
            
            request.session["uname"]=uname
            data={"status":"Customer"}
            return JsonResponse(data,safe=False)
        except:
            data={"status":0}
            return JsonResponse(data,safe=False)
    else:
        data={"status":0}
        return JsonResponse(data,safe=False)


def About_page(request):
    return render(request,'About_page.html',{})

def Customer_home(request):
    
    return render(request,'Customer_home.html',{})


def Volunteer_home(request):
    
    return render(request,'Volunteer_home.html',{})




def Customer_add_request(request):
    
    return render(request,'Customer_add_request.html',{})



from datetime import datetime



@ensure_csrf_cookie
def Add_request_data(request):
    uname=request.session["uname"]
    # uname="Suraj123"
    data={}
    if request.method == "GET":
        return render(request, 'Shophome.html', )
    if request.method == 'POST':
        files = request.FILES.getlist('files[]', None)
        print("files==>",files)
        addr=request.POST.get("addr")
        des=request.POST.get("des")
        latval=request.POST.get("latval")
        longval=request.POST.get("longval")
        # datetime object containing current date and time
        now = datetime.now()
        
        print("now =", now)
        
        # dd/mm/YY
        dt_string = now.strftime("%d_%m_%Y_%H_%M_%S")
        print("d1 =", dt_string)
        dt_val = now.strftime("%d/%m/%Y")
        print("dt_val =", dt_val)
        try:
            imgpath=dt_string+".jpg"
            for f in files:
                handle_uploaded_file(f,imgpath)

            imp='PID_app/static/Wastes/'+imgpath
            wtype=detect1(imp)
            print("detected garbages-->",wtype)
            ob1=Waste_table(Uname=uname,Latitude=latval,Longitude=longval,Address=addr,Description=des,Image_path=imgpath,
                           Waste_types=wtype,Date=dt_val)
            ob1.save()

            data["result"]="yes"
            return JsonResponse(data,safe=False)
        except:
                    
            data["result"]="no"
            print (data)
            return JsonResponse(data,safe=False)
    else:
        data["result"]="error"
        print (data)
        return JsonResponse(data,safe=False)

def handle_uploaded_file(f,name):
    print("imagename-->",name)
    filename='PID_app/static/Wastes/'+str(name)
    with open(filename, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)



def Customer_view_requests(request):
    uname=request.session["uname"]
    # uname="Suraj123"
    ob=Waste_table.objects.filter(Uname=uname)
    return render(request,'Customer_view_rqst.html',{'data':ob})



def Volunteer_view_request(request):
    ob=Waste_table.objects.filter(Vstatus="Not accepted")
    return render(request,'Volunteer_view_rqst.html',{"data":ob})







def Accept_wrequest(request):
    uname=request.session["uname"]
    # uname="kishor123"
    obusr=Volunteer_reg.objects.get(Username=uname)
    vname=obusr.Name
    data={}
    cid=request.GET.get("uid")
    ob=Waste_table.objects.get(id=int(cid))
    ob.Vstatus=vname
    ob.Vuname=uname
    ob.save()
    
    data["status"]="yes"
    print (data)
    return JsonResponse(data,safe=False)



def Volunterr_accepted_requests(request):
    uname=request.session["uname"]
    # uname="kishor123"
    ob=Waste_table.objects.filter(Vuname=uname,Status="Not completed")
    return render(request,'Volunteer_accepted.html',{"data":ob})





def Get_waste_loc(request):
    data={}
    cid=request.GET.get("uid")
    uname=request.session["uname"]
    # uname="maski123"
    ob=Waste_table.objects.get(id=int(cid))
    dlat=ob.Latitude
    dlong=ob.Longitude
    if(dlat=="0" or dlong==0):
         data["status"]=0
    else:
        data["status"]=1
        data['lat']=dlat
        data['long']=dlong
    print (data)
    return JsonResponse(data,safe=False)



def Volunterr_view_map(request):
    return render(request,'Volunteer_map_page.html',{})



def Save_waste_id(request):
    data={}
    cid=request.GET.get("uid")
    request.session['wid']=cid
    
    data["status"]=1
    print (data)
    return JsonResponse(data,safe=False)



def Volunterr_edit_waste(request):
    cid=request.session['wid']
    ob=Waste_table.objects.get(id=int(cid))
    return render(request,'Volunteer_edit_waste.html',{"data":ob})


def Update_status(request):
    data={}
    wid=request.GET.get("uid")
    reqval=request.GET.get("reqval")
    try:
        ob=Waste_table.objects.get(id=int(wid))
        ob.Reqstatus=reqval
        ob.save()
        data["status"]="yes"
    except:
        data["status"]="no"
    print (data)
    return JsonResponse(data,safe=False)


def Update_work(request):
    data={}
    wid=request.GET.get("uid")
    try:
        ob=Waste_table.objects.get(id=int(wid))
        ob.Status="Completed"
        ob.save()
        data["status"]="yes"
    except:
        data["status"]="no"
    print (data)
    return JsonResponse(data,safe=False)








def Volunteer_view_route(request):
    return render(request,'Volunteer_route.html',{})

def Volunteer_get_locations(request):
    uname=request.session["uname"]
    # uname="Ak1234"
    ob=Waste_table.objects.filter(Vuname=uname,Status="Not completed")
    data={}

    mainlist=[]
    cnt=1
    for i in ob:
         liloc=[]
         liloc.append(i.Address)
         liloc.append(float(i.Latitude))
         liloc.append(float(i.Longitude))
         liloc.append(cnt)
         cnt+=1
         mainlist.append(liloc)


        
    data["loclist"]=mainlist

    print(data)
    return JsonResponse(data,safe=False)

def Volunteer_list_user_page(request):
    uname=request.session["uname"]
    # uname="Ak1234"
    ob=Waste_table.objects.filter(Vuname=uname)
    mainlist=[]
    for i in ob:
         li1=[]
         duname=i.Uname
         li1.append(duname)
         ob=Customer_reg.objects.get(Username=duname)
         li1.append(ob.Name)
         obc=Chat_table.objects.filter(From=duname,To=uname,sts="not read")
         cnt=obc.count()
         if(cnt==0):
            li1.append("")
         else:
              li1.append(cnt)
         if (li1 not in mainlist):
            mainlist.append(li1)
    print(mainlist)
    return render(request,'Volunteer_list_user.html',{"data":mainlist})


def Volunteer_chat_page(request):
    user2=request.session['user2id']
    ob=Customer_reg.objects.get(Username=user2)
    name=ob.Name
    request.session['user2name']=name
    return render(request,'Volunteer_chat_page.html',{"name":name})


def Save_user2_id(request):
    print("saving to id")
    data={}
    uname=request.session["uname"]
    # uname="Abhi123"
    print(uname)
    unameid=request.GET.get("idval")
    ob=Chat_table.objects.filter(To=unameid)|Chat_table.objects.filter(From=unameid)
    for i in ob:
         
         print("to-->",i.To)
         if(i.To==uname):
            i.sts="read"
            i.save()
   
    request.session['user2id']=unameid
    data["status"]=1
    print (data)
    return JsonResponse(data,safe=False)




def Customer_list_user_page(request):
    uname=request.session["uname"]
    # uname="Aswin123"
    ob=Waste_table.objects.filter(Uname=uname)
    mainlist=[]
    for i in ob:
         li1=[]
         if((i.Vstatus)!="Not accepted"):
            duname=i.Vuname
            li1.append(duname)
            li1.append(i.Vstatus)
            obc=Chat_table.objects.filter(From=duname,To=uname,sts="not read")
            cnt=obc.count()
            if(cnt==0):
                li1.append("")
            else:
                li1.append(cnt)
            if (li1 not in mainlist):
                mainlist.append(li1)
    print(mainlist)
    return render(request,'Customer_list_user.html',{"data":mainlist})




def Customer_chat_page(request):
    user2=request.session['user2id']
    ob=Volunteer_reg.objects.get(Username=user2)
    name=ob.Name
    request.session['user2name']=name
    return render(request,'Customer_chat_page.html',{"name":name})





def Save_user2_id(request):
    print("saving to id")
    data={}
    uname=request.session["uname"]
    # uname="Abhi123"
    print(uname)
    unameid=request.GET.get("idval")
    ob=Chat_table.objects.filter(To=unameid)|Chat_table.objects.filter(From=unameid)
    for i in ob:
         
         print("to-->",i.To)
         if(i.To==uname):
            i.sts="read"
            i.save()
   
    request.session['user2id']=unameid
    data["status"]=1
    print (data)
    return JsonResponse(data,safe=False)



def Addchat(request):
    msg=request.GET.get("qstn")
    sndr=request.session["uname"]
    
    # sndr="Abhi123"
    rcvr=request.session['user2id']
    print(sndr,"--->",rcvr)
    ob=Chat_table(From=sndr,To=rcvr,chat=msg)
    ob.save()
    data={"msg":"yes"}
    return JsonResponse(data,safe=False)


def Getallchats(request):
    sndr=request.session["uname"]
    # sndr="Aswin123"
    rcvr=request.session['user2id']
    dname=request.session['user2name']
    ob=Chat_table.objects.filter(From=sndr,To=rcvr) | Chat_table.objects.filter(From=rcvr,To=sndr) 
    mylist=[]
    for i in ob:
        li1=[]
        if(i.From==sndr):
            li1.append("You")
            print(i.From)
     
        else:
            unme=i.To
            print("driver-->",unme)
            # ob0=Driver_reg.objects.get(Username=unme)
            # dname=ob0.Name
            # print(dname)
            li1.append(dname)
        li1.append(i.chat)
        mylist.append(li1)
    print("mylist-->",mylist)
    resp={}
    resp["datalist"]=mylist
    return JsonResponse(resp,safe=False)








#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
















