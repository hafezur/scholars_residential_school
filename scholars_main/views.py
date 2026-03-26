from django.shortcuts import render
from.models import okgs_photo,scientest,NewsEvent ,singleUnique
# Create your views here.
def home_function(request):
    principal_pic = singleUnique.objects.filter(title='omar').latest('created_at')
    for_gallery = okgs_photo.objects.all()[1:12]
    for_carusol= okgs_photo.objects.all()[1:]
    get_scientest=scientest.objects.all()
    logo = singleUnique.objects.filter(title='school_logo').latest('created_at')
    
    context = {
        "principal_pic": principal_pic,
        "for_gallery": for_gallery,
        "for_carusol": for_carusol,
        "get_scientest": get_scientest,
        "logo": logo,
        'students_count': 1000,
        'teachers_count': 80,
        'staff_count': 50,
    }

    return render(request, "home.html",context)


def about_function(request):
    logo = singleUnique.objects.filter(title='school_logo').latest('created_at')
    context={
        'logo':logo,
    }
    return render(request,"about.html",context)


def feature_function(request):
    logo = singleUnique.objects.filter(title='school_logo').latest('created_at')
    context={
        'logo':logo,
    }
    return render(request,'feature.html',context)

def galary_function(request):
    for_gallery = okgs_photo.objects.all()[1:]
    for_carusol= okgs_photo.objects.all()[2:7]
    logo = singleUnique.objects.filter(title='school_logo').latest('created_at')
    context = {
        "for_gallery": for_gallery,
        "logo": logo,
        
    }

    return render(request, "galary.html", context)

def contact(request):
    logo = singleUnique.objects.filter(title='school_logo').latest('created_at')
    context={
        'logo':logo,
    }
    return render(request,'contact.html',context)

def newsEvent(request):
    item=NewsEvent.objects.all()
    logo = singleUnique.objects.filter(title='school_logo').latest('created_at')
    context={
        'item':item,
        'logo':logo,
    }
    return render(request,"news&event.html",context)