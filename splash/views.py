from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'title': "Hello from index!!"}
    return render(request, 'index.html', context=context)

def page_one(request):
    context = {'title': "Hello from page one!!"}
    # If the request is not from the HX client, return the full page
    if request.META.get("HTTP_HX_REQUEST") != 'true':
        print("Not an HX request")
        return render(request, 'page_one_full.html', context=context)
    # Otherwise, return the partial page
    return render(request, 'page_one.html', context=context)

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