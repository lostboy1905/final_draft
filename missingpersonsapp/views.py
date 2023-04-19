from django.shortcuts import render, redirect
from .models import Missing

def indexPageView(request) :
    return render(request, 'missingpersonsapp/index.html')

def BYUPageView(request) :
    return render(request, 'missingpersonsapp/BYU.html')

def contactPageView(request) :
    return render(request, 'missingpersonsapp/contact.html')

def projectsPageView(request) :
    return render(request, 'missingpersonsapp/projects.html')

def viewmissingpersonsPageView(request):
    data = Missing.objects.all()

    if data.count() == 0:
        error_message = "Not found"
    else:
        error_message = ""

    context = {
        "missing_persons": data,
        "error": error_message
        }
    return render(request, "missingpersonsapp/viewmissingpersons.html", context)

def addmissingpersonsPageView(request) :
    if request.method == 'POST':
        new_missing = Missing()
        new_missing.Date_Missing = request.POST.get("dateMissing")
        new_missing.First_Name = request.POST.get("firstName")
        new_missing.Last_Name = request.POST.get("lastName")
        new_missing.age_at_missing = request.POST.get("ageAtMissing")
        new_missing.city = request.POST.get("city")
        new_missing.state= request.POST.get("state")
        new_missing.gender = request.POST.get("gender")
        new_missing.race = request.POST.get("race")
        new_missing.save()
    return render(request, "missingpersonsapp/viewmissingpersons.html")

def editmissingpersonsPageView(request, sFirstName):
    person = Missing.objects.get(id=sFirstName)
    
    if request.method == 'Post':
        person.Date_Missing = request.POST.get("dateMissing")
        person.First_Name = request.POST.get("firstName")
        person.Last_Name = request.POST.get("lastName")
        person.age_at_missing = request.POST.get("ageAtMissing")
        person.city = request.POST.get("city")
        person.state= request.POST.get("state")
        person.gender = request.POST.get("gender")
        person.race = request.POST.get("race")
        person.save()
        return redirect(viewmissingpersonsPageView)
    
    context={
        "missing_persons": person
    }
    return render(request, "missingpersonsapp/editmissingpersons.html", context)

def searchmissingpersonsPageView(request):
    sFirst = request.GET['firstName']
    sLast = request.GET['lastName']
    data = Missing.objects.filter(First_Name=sFirst, Last_Name=sLast)

    if data.count() == 0:
        error_message = "Not found"
    else:
        error_message = ""

    context = {
        "missing_persons": data,
        "message": error_message
        }
    return render(request, 'missingpersonsapp/viewmissingpersons.html', context)