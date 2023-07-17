from django.shortcuts import render

# Create your views here.
def index(request):
    """View function for home page of site."""

    context = {
        'test': 123,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)