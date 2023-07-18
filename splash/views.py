from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'title': "Hello from index!!"}
    return render(request, 'index.html', context=context)

def page1(request):
    context = {'title': "Hello from page 1!!"}
    # If the request is not from the HX client, return the full page
    if request.META.get("HTTP_HX_REQUEST") != 'true':
        print("Not an HX request")
        return render(request, 'page1_full.html', context=context)
    # Otherwise, return the partial page
    return render(request, 'page1.html', context=context)

def page2(request):
    context = {'title': "Hello from page 2!!"}
    # If the request is not from the HX client, return the full page
    if request.META.get("HTTP_HX_REQUEST") != 'true':
        print("Not an HX request")
        return render(request, 'page2_full.html', context=context)
    # Otherwise, return the partial page
    return render(request, 'page2.html', context=context)

def page3(request):
    context = {'title': "Hello from page 3!!"}
    # If the request is not from the HX client, return the full page
    if request.META.get("HTTP_HX_REQUEST") != 'true':
        return render(request, 'page3_full.html', context=context)
    # Otherwise, return the partial page
    return render(request, 'page3.html', context=context)