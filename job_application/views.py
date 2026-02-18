from django.shortcuts import render
from .forms import ApplicationForm


#
def index(request):
    """
    HOME PAGE
    This function is used to render the index.html file whenever the index page (http://127.0.0.1:8000/) is requested
    """
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        # form validation
        if form.is_valid():
            # make sure the name corresponds to the name in the html
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            occupation = form.cleaned_data["occupation"]
            print(first_name, last_name, email, date, occupation)
        else:
            print(form.errors)

    return render(request, "index.html")
