from django.shortcuts import render
from .forms import NameForm
from django.http import HttpResponseRedirect
from shopUsers.models import Product

# Create your views here.


def get_name(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("/thanks/")
    else:
        form = NameForm()
    return render(request, "name.html", {"form": form})


def add_comment(request):
    post = Product.objects.get(id=1)
