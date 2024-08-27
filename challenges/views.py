from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
def monthly_challenge_by_number(request, month):
    if month == 1:
        challenge_text = "Eat no meat for the entire month!"
    elif month == 2:
        challenge_text = "Walk for at least 20 minutes every day!"
    elif month == 3:
        challenge_text = "Learn Django for at least 20 minutes every day!"
    else:
        return HttpResponseNotFound("This month is not supported!")

    return HttpResponse(challenge_text)

def monthly_challenges(request, month):
    if month == "january":
        challenge_text = "Eat no meat for the entire month!"
    elif month =="february":
        challenge_text = "Walk for at least 20 minutes every day!"
    elif month == "march":
        challenge_text = "Learn Django for at least 20 minutes every day!"
    else:
        return HttpResponseNotFound("This month is not supported!")

    return HttpResponse(challenge_text)