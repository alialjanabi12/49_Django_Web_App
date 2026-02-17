from django.shortcuts import render


#
def index(requests):
    """
    HOME PAGE
    This function is used to render the index.html file whenever the index page (http://127.0.0.1:8000/) is requested
    """
    return render(requests, "index.html")
