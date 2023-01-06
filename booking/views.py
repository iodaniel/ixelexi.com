from django.shortcuts import render, redirect 
from datetime import datetime, timedelta
from .models import *
from django.contrib import messages

def index(request):
    return render(request, 'index.html',{
        
    })

# Create your views here.
def booking(request):
    weekdays = validWeekday(22)
    validateWeekdays = isWeekdayValid(weekdays)

    if request.method=='POST':
        service = request.POST.get('service')
        day = request.POST.get('day')
        if service == None:
            messages.success(request, "Please Select a Service!")
            return redirect('booking')

        request.session['day']= day
        request.session['serivce']= service

        return redirect('bookingSubmit')

    return render(request, 'booking.html', {
        'weekdays':weekdays,
        'validateWeekdays':validateWeekdays,
    
    
    })
def bookingSubmit(request):
    user = request.user
    time= [
        "10:00 AM",  "11:00 AM", "12:00 PM", "1:00 PM", "3:00 PM",
"4:00 PM", "5:00 PM", "6:00 PM"

    ]
    today = datetime.now()
    minDate = today.strftime("%Y-%m-%d")
    deltatime = today + timedelta(days=21)
    strdeltatime = deltatime.strftime("%Y-%m-%d")
    maxDate = strdeltatime

    day = request.session.get('day')
    service = request.session.get('service')

    hour = checkTime(time,day)
    if request.method =="POST":
        time = request.POST.get("time")
        date = dayToWeekday(day)

        if service != None:
            if day <= maxDate and day >= minDate:
                if date == 'Monday' or date =='Saturday' or date =='Wednesday':
                    if Appointment.objects.filter(day=day).count() < 11:
                        if Appointment.objects.filter(day=day, time=time).count()<1:
                            AppointmentForm = Appointment.objects.get_or_create(
                                user= user, 
                                service = service,
                                day = day, 
                                time = time,

                            ) 
                            messages.success(request, "Appoinment Saved!")
                            return redirect('index')

                        else:
                            messages.success(request, "The selected time has been reserved before for another customer")
                    else:
                        messages.success(request, "The Selected Day Is Full!!")
                else: 
                    messages.success(request, "The Selected Day Is Incorrect")
            else:
                messages.success(request, "The selected Date Isn't In The Correct Time Period!")
        else:
            messages.success(request, "Please Select A Service!")

    return render(request, 'bookingSubmit.html', {
        'times':hour,
    })
def userPanel(request, id):
    user = request.user
    appointments= Appointment.objects.filter(user=user).order_by('day', 'time')
    return render(request, 'userPanel.html',{
        'user':user,
        'appointments': appointments,

    })

def userUpdate(request, id):
    appointment = Appointment.objects.get(pk=id)
    userdatepicked = appointment.day
    today = datetime.today()
    minDate = today.strftime('%Y-%m-%d')

    delta24 = (userdatepicked).strftime('%Y-%m-%d')>= (today + timedelta(days=1)).strftime('%Y-%m-%d')
    weekdays = validWeekday(22)

    validateWeekdays = isWeekdayValid(weekdays)

    if request.method =="POST":
        service = request.POST.get('service')
        day = request.POST.get('day')
        request.session['day'] = day
        request.session['service']= service

        return redirect('userUpdateSubmit', id=id)

    return render(request, 'userUpdate.html',{
        'weekdays':weekdays,
        'validateWeekdays':validateWeekdays,
        'delta24': delta24,
        'id': id, 



    })

def userUpdateSubmit(request, id):
    user = request.user
    times = [
         "10:00 AM",  "11:00 AM", "12:00 PM", "1:00 PM", "3:00 PM",
"4:00 PM", "5:00 PM", "6:00 PM"
    ]
    today = datetime.now()
    minDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=21)
    strdeltatime = deltatime.strftime('%Y-%m-%d')
    maxDate = strdeltatime

    day = request.session.get('day')
    service = request.session.get('service')
    
    #Only show the time of the day that has not been selected before and the time he is editing:
    hour = checkEditTime(times, day, id)
    appointment = Appointment.objects.get(pk=id)
    userSelectedTime = appointment.time
    if request.method == 'POST':
        time = request.POST.get("time")
        date = dayToWeekday(day)

        if service != None:
            if day <= maxDate and day >= minDate:
                if date == 'Monday' or date == 'Tuesday' or date == 'Wednesday' or date == 'Thursday'  or date == 'Friday' or date == 'Saturday' :
                    if Appointment.objects.filter(day=day).count() < 11:
                        if Appointment.objects.filter(day=day, time=time).count() < 1 or userSelectedTime == time:
                            AppointmentForm = Appointment.objects.filter(pk=id).update(
                                user = user,
                                service = service,
                                day = day,
                                time = time,
                                
                            ) 
                            messages.success(request, "Appointment Edited!")
                            return redirect('index')
                        else:
                            messages.success(request, "The Selected Time Has Been Reserved Before!")
                    else:
                        messages.success(request, "The Selected Day Is Full!")
                else:
                    messages.success(request, "The Selected Date Is Incorrect")
            else:
                    messages.success(request, "The Selected Date Isn't In The Correct Time Period!")
        else:
            messages.success(request, "Please Select A Service!")
        return redirect('userPanel')


    return render(request, 'userUpdateSubmit.html', {
        'times':hour,
        'id': id,
    })

def staffPanel(request):
    today = datetime.today()
    minDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=21)
    strdeltatime = deltatime.strftime('%Y-%m-%d')
    maxDate = strdeltatime
    #Only show the Appointments 21 days from today
    items = Appointment.objects.filter(day__range=[minDate, maxDate]).order_by('day', 'time')

    return render(request, 'staffPanel.html', {
        'items':items,
    })

def dayToWeekday(x):
    z = datetime.strptime(x, "%Y-%m-%d")
    y = z.strftime('%A')
    return y

def validWeekday(days):
    #Loop days you want in the next 21 days:
    today = datetime.now()
    weekdays = []
    for i in range (0, days):
        x = today + timedelta(days=i)
        y = x.strftime('%A')
        if y == 'Monday' or y == 'Saturday' or y == 'Wednesday':
            weekdays.append(x.strftime('%Y-%m-%d'))
    return weekdays
    
def isWeekdayValid(x):
    validateWeekdays = []
    for j in x:
        if Appointment.objects.filter(day=j).count() < 10:
            validateWeekdays.append(j)
    return validateWeekdays

def checkTime(times, day):
    #Only show the time of the day that has not been selected before:
    x = []
    for k in times:
        if Appointment.objects.filter(day=day, time=k).count() < 1:
            x.append(k)
    return x

def checkEditTime(times, day, id):
    #Only show the time of the day that has not been selected before:
    x = []
    appointment = Appointment.objects.get(pk=id)
    time = appointment.time
    for k in times:
        if Appointment.objects.filter(day=day, time=k).count() < 1 or time == k:
            x.append(k)
    return x