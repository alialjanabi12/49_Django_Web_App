from math import e
from django.shortcuts import render

# the ". " means "from the current directory"
from .forms import ApplicationForm
from .models import Database_From
from django.contrib import messages
from django.core.mail import EmailMessage


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
            # print(first_name, last_name, email, date, occupation)

            Database_From.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                date=date,
                occupation=occupation,
            )

            message_body = f" A new job application was submitted.\nThank you,\n{first_name} {last_name} "
            email_message = EmailMessage(
                subject="New Job Application",
                body=message_body,
                to=[email],
            )
            email_message.send()

            messages.success(request, "Your application has been submitted")

    return render(request, "index.html")


def about(request):
    return render(request, "about.html")
