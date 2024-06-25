# from telnetlib import LOGOUT
from datetime import date
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Notes
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from gfg import settings
from django.core.mail import send_mail

# import os
# from django.conf import settings
from django.template.loader import get_template
from xhtml2pdf import pisa


# from django.contrib.staticfiles import finders
# from django.shortcuts
# Create your views here.
ouruser = ""


def home(request):
    return render(request, "authentication/index.html")


def signup(request):
    if request.method == "POST":
        # username = request.POST.get('username')
        username = request.POST["username"]
        ouruser = username
        email = request.POST.get("email")
        pass1 = request.POST.get("pass1")
        pass2 = request.POST.get("pass2")

        if User.objects.filter(username=username):
            messages.error(request, "Username already exists! PLease try other")

        # if User.objects.filter(email = email):
        #     messages.error(request, "Email already registered")

        if pass1 != pass2:
            messages.error(request, "Both the passwords are not matching")

        myUser = User.objects.create_user(username, email, pass1)
        # User.objects.create
        myUser.save()

        messages.success(
            request,
            "Your account has been successfully created. \n We have sent you a confirmation mail",
        )

        # Welcome Email
        subject = "Welcome to Book Drive"
        message = (
            "Hello "
            + username
            + "! \n"
            + "Thank You for visiting our website \n We have completed the website development process and glad to tell you that are registered"
        )
        from_email = settings.EMAIL_HOST_USER
        to_list = [myUser.email]
        send_mail(subject, message, from_email, to_list)

        return redirect("/signin")

    return render(request, "authentication/signup.html")


def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        pass1 = request.POST.get("pass1")
        user = authenticate(username=username, password=pass1)
        notes = Notes.objects.all()
        # ouruser = username

        if user is not None:
            if user.is_staff:
                login(request, user)
                # fname = user.first_name
                return render(
                    request,
                    "authentication/bookDrive.html",
                    {"username": username, "notes": notes},
                )
            else:
                login(request, user)
                # fname = user.first_name
                return render(
                    request,
                    "authentication/index.html",
                    {"username": username, "notes": notes},
                )
        else:
            messages.error(request, "Bad Credentials")
            return redirect("home")

    return render(request, "authentication/signin.html")


def signout(request):
    logout(request)
    # User.objects.filter(given_name!='').delete()
    messages.success(request, "Logged out successfully")
    return redirect("home")


def render_pdf_view(request):
    pass


#     template_path = 'https://northell.design/wp-content/uploads/2021/11/A_Complete_Web_Development_Guide_For_Non_Technical_Startup_Founder.pdf'
#     context = {'myvar': 'this is your template context'}
#     # Create a Django response object, and specify content_type as pdf
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="report.pdf"'
#     # find the template and render it.
#     template = get_template(template_path)
#     html = template.render(context)

#     # create a pdf
#     pisa_status = pisa.CreatePDF(
#        html, dest=response)#, link_callback=link_callback)
#     # if error then show some funny view
#     if pisa_status.err:
#        return HttpResponse('We had some errors <pre>' + html + '</pre>')
#     return response


def bookDrive(request):
    # if not request.user.is_authenticated:
    #     return redirect('home')
    # error = "You are not logged in"
    if request.method == "POST":
        # name = request.POST.get("name")
        # description = request.POST.get("description")
        # file = request.FILES.get("file")
        # notes = Notes.objects.create(
        #     uploadingdate=date.today(), Description=description, Name=name, File=file
        # )
        # # User.objects.create
        # notes.save()
        notes = Notes.objects.all()
        messages.success(request, "bookDrive Submission done successfully")
        return render(
            request,
            "authentication/bookDrive.html",
            {"username": ouruser, "notes": notes},
        )
    return render(request, "authentication/bookDrive.html")


def upload(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        file = request.FILES.get("file")
        notes = Notes.objects.create(
            uploadingdate=date.today(), Description=description, Name=name, File=file
        )
        # User.objects.create
        notes.save()
        notes = Notes.objects.all()
        # messages.success(request, "bookDrive Submission done successfully")
        return render(
            request,
            "authentication/bookDrive.html",
            {"username": ouruser, "notes": notes},
        )
    return render(request, "authentication/upload.html")


def google(request):
    if request.method == "POST":
        # username = request.POST["username"]
        # # pass1 = request.POST.get("pass1")
        # user = authenticate(username=username)
        notes = Notes.objects.all()
        # # ouruser = username

        # if user is not None:
        #     if user.is_staff:
        #         # print(notes)
        #         login(request, user)
        #         # fname = user.first_name
        #         return render(
        #             request, "authentication/bookDrive.html",# {"username": username , "notes": notes}
        #         )
        #     else:
        #         login(request, user)
        #         # fname = user.first_name
        #         return render(
        #             request, "authentication/index.html",# {"username": username,"notes": notes}
        #         )
        # else:
        #     messages.error(request, "Bad Credentials")
        #     return redirect("home")

    return render(request, "authentication/google.html", {"notes": notes})


def viewfile(request):
    notes = Notes.objects.all()
    # if user is not None:
    #     if user.is_staff:
    #         # print(notes)
    #         login(request, user)
    #         # fname = user.first_name
    #         return render(
    #             request, "authentication/bookDrive.html",# {"username": username , "notes": notes}
    #         )
    #     else:
    #         login(request, user)
    #         # fname = user.first_name
    #         return render(
    #             request, "authentication/index.html",# {"username": username,"notes": notes}
    #         )
    return render(request, "authentication/viewfile.html", {"notes": notes})
