from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegistrationForm
from .forms import LoginForm,BookingForm
from .models import Roominformation,Bookingdetails1,Hotelinfo
from django.db.models import Q
from django.http import HttpResponse

# Create your views here.
def login_user(request):
    if request.method == "POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user=authenticate(request, username=cd['username'],password=cd['password'])

            if user is not None:
                login(request, user)
                return redirect('Search')
            else:
                return redirect('/')

    else:
        form=LoginForm()
        return render(request, 'login.html',{'form':form})

def register(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        password_repeat = request.POST["password_repeat"]
        
        email = request.POST["email"]
        

        if password_repeat == password:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email Taken")
                return redirect('register')

            else:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password
                )
                
                user.save()
        else:
            print("password not matching...")
        return redirect('/')
    else:
        return render(request, 'register.html')

def Search(request):
    if request.method=="POST":
        sdate1 = request.POST['sdate']
        edate1 = request.POST['edate']

        if sdate1 and edate1:
            match= Roominformation.objects.filter(Q(sdate__lte=sdate1) & Q(edate__gte=edate1) & Q(sdate__lte=edate1) & Q(edate__gte=sdate1))
            if match:
                return render(request,'result.html',{'sd':match})
            else:
                messages.error(request,"No result found")
        else:
            return redirect('Search')
    return render(request,"search.html")

def RoomInfo(request):
    rooms=Roominformation.objects.all().select_related('hotel')
    
    return render(request, 'RoomType.html', {'rooms':rooms})

def booking(request):
    if request.method== 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_name = request.POST['user_name']
        email = request.POST['email']
        phone = request.POST['phone']
        startdate = request.POST['startdate']
        enddate = request.POST['enddate']
        hotel1_n = request.POST.get('hotel1')    
        room1_n= request.POST.get('room1')
    
        
        address1 = request.POST['address1']
        
        user1 = Bookingdetails1.objects.create( first_name=first_name, 
                                               last_name=last_name,
                                               user_name = user_name,
                                               email = email,
                                               phone=phone,
                                               startdate = startdate,
                                               enddate = enddate,
                                               hotel1_id=hotel1_n,
                                               room1_id=room1_n,
                                               address1 = address1)
        user1.save()
        return render(request,"final.html")
         
    else:
        return render(request,"HotelPnrDisplay.html")

def reserve(request):
    if request.method=="POST":
        usname = request.POST['username']

        if usname:
            match = Bookingdetails1.objects.filter(user_name=usname)
            if match:
                return render(request,'reserve.html',{'sd':match})
            else:
                messages.error(request,"No result found")
        else:
            return redirect('reserve')
    return render(request,"roomcheck.html")


    



