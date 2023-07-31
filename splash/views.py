from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import FormOne

# Create your views here.
def index(request):
    context = {'title': "Hello from index!!"}
    return render(request, 'index.html', context=context)

def page_one(request):
    # If the request is not from the HX client, return the full page
    # This handles the case of page refreshes, etc.
    if request.META.get("HTTP_HX_REQUEST") != 'true':
        form = FormOne(request.POST)
        print("Not an HX request")
        return render(request, 'page_one_full.html', {"form": form})
    
    # If a POST, create a form instance and populate it with data from the request
    if request.method == "POST":
        form = FormOne(request.POST)
        # Check whether it's valid:
        if form.is_valid():
            # Process the data in form.cleaned_data as required
            # ...
            # Save the form
            form.save()
            # redirect to a new URL:
            url = reverse("page_one_success")
            return HttpResponseRedirect(url)

    # If a GET (or any other method) we'll create a blank form
    else:
        form = FormOne()

    # Otherwise, return the partial page
    return render(request, "page_one.html", {"form": form})

def page_one_success(request):
    context = {'title': "Hello from page one success!!"}
    # Return the partial page
    return render(request, 'page_one_success.html', context=context)

def page_two(request):
    context = {'title': "Hello from page two!!"}
    # If the request is not from the HX client, return the full page
    if request.META.get("HTTP_HX_REQUEST") != 'true':
        print("Not an HX request")
        return render(request, 'page_two_full.html', context=context)
    # Otherwise, return the partial page
    return render(request, 'page_two.html', context=context)

def page_three(request):
    context = {'title': "Hello from page three!!"}
    # If the request is not from the HX client, return the full page
    if request.META.get("HTTP_HX_REQUEST") != 'true':
        return render(request, 'page_three_full.html', context=context)
    # Otherwise, return the partial page
    return render(request, 'page_three.html', context=context)