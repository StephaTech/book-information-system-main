from django.shortcuts import render
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render, redirect
# Create your views here.
from .models import * #the * means that I will import evertything that is in models.py

#from bis_portal.bis_app.models import member

#These are functions
def home(request):
    return render(request,"home.html" , context={"current_tab": "home"})

def members(request):
    return render(request,"members.html" , context={"current_tab": "members"})

def books(request):
    return render(request,"books.html" , context={"current_tab": "books"})

def shopping(request):
    return HttpResponse("Welcome to shopping")    

def save_member(request):
    member_name = request.POST['member_name']
    #return HttpResponse("Welcome to Book Library - "+ member_name) #will retrieve name typed on the web and displayed on the web
    return render(request,"welcome.html", context={'member_name':member_name})

def members_tab(request):
    if request.method=="GET":
        members = member.objects.all()
        return render(request,"members.html",
                  context={"current_tab": "members",
                           "members":members}
                ) #observe that I am calling the members.html page
    else:
        query = request.POST['query']
        members = member.objects.raw("select * from bis_app_member where member_name like '%"+query+"%'")
        return render(request,"members.html",
                  context={"current_tab": "members",
                           "members":members,"query": query}
                ) #observe that I am calling the members.html page
    

    
def save_member(request): #path('members/add', save_member),path('save', save_member),
    # Creating a property for model member
    member_item = member(reference_id=request.POST['member_reference_id'],
                         member_name=request.POST['member_name'],
                         member_contact=request.POST['member_contact'],
                         member_country=request.POST['member_country'],
                         active=True
                         )

    member_item.save()
    return redirect('/members') #help to reload the page

def update_member(request):
            id = request.POST.get("id")
            member_name = request.POST.get("member_name")
            member_contact = request.POST.get("member_contact")
            member_reference_id = request.POST.get("member_reference_id")
            member_country = request.POST.get("member_country")
            members =member.objects.get(id=id)
            member.member_name = member_name
            member.member_contact = member_contact
            member.reference_id = member_reference_id
            member.member_country = member_country
            members.save()
            return redirect('/members')
            #messages.success(request, "student updated successfully")

# def update_member(request):
#             id = request.POST.get("id")
#             member_name = request.POST.get("member_name")
#             member_contact = request.POST.get("member_contact")
#             member_reference_id = request.POST.get("member_reference_id")
#             member_country = request.POST.get("member_country")
#             members =member.objects.get(id=id)
#             member.member_name = member_name
#             member.member_contact = member_contact
#             member.reference_id = member_reference_id
#             member.member_country = member_country
#             members.save()
#             return redirect('/members')
#             #messages.success(request, "student updated successfully")

# def delete_member(request):
#     members = member.objects.get(members)

#     if request.method == 'POST':
#         members.delete()
#         return redirect('/members')

#     context = {'members' :members}
#     return render(request, 'members.html', context)

# def delete_member(request): 
#     # Creating a property for model member
#     member_item = member(reference_id=request.POST['member_reference_id'],
#                          member_name=request.POST['member_name'],
#                          member_contact=request.POST['member_contact'],
#                          member_country=request.POST['member_country'],
#                          active=True
#                          )

#     member_item.delete()
#     return redirect('/members') #help to reload the page