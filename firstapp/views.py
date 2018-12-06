from django.shortcuts import render
from .forms import SubscriberForm


def index(request):
    name = "Yukish Ivan"
    curren_day = "04.12.2018"

    form = SubscriberForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data["name"])

        new_form = form.save()
    else:
        print("not found")
    return render(request, "firstapp/index.html", locals())


def home(request):

    return render(request, "firstapp/home.html", locals())
