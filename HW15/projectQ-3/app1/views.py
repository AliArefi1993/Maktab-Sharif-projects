from django.shortcuts import render
from .forms import NameForm
from django.http import HttpResponseRedirect
# Create your views here.


def get_name(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("/thanks/")
    else:
        form = NameForm()
    return render(request, "name.html", {"form": form})
