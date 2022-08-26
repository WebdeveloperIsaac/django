from django.shortcuts import render
from django import forms
# Create your views here.

tasks=["hello" , "hai" ,"bye" ]

class NewForm(forms.Form):
    task = forms.CharField(label="Enter the Task to Be added:")

def index(request):
    return render(request,"taskm/index.html",{
        "task":tasks
    })

def add(request):
    if request.method=="POST":
        form = NewForm(request.POST)
        if form.is_valid():
            task= form.cleaned_data["task"]
            tasks.append[task]
        else:
            return render(request,"taskm/add.html",{
                "form":form
            })    
    return render(request,"taskm/add.html",{
        "form":NewForm()
    })    