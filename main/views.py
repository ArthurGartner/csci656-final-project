from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect

# Create your views here.


def page_index(request):
    return render(request=request,
                  template_name="main/page_index.html",
                  context={"loggedin": request.user.is_authenticated})


def page_about(request):
    return render(request=request,
                  template_name="main/page_about.html",
                  context={"loggedin": request.user.is_authenticated})


def page_checklist(request):
    return render(request=request,
                  template_name="main/page_checklist.html",
                  context={"loggedin": request.user.is_authenticated})


def page_future_work(request):
    return render(request=request,
                  template_name="main/page_future_work.html",
                  context={"loggedin": request.user.is_authenticated})


def page_login(request):
    return render(request=request,
                  template_name="main/page_login.html",
                  context={"loggedin": request.user.is_authenticated})


def page_signup(request):
    return render(request=request,
                  template_name="main/page_signup.html",
                  context={"loggedin": request.user.is_authenticated})

def page_job_dashboard(request):
    if not request.user.is_authenticated:
        return page_login(request)

    return render(request=request,
                  template_name="main/page_jobs_dashboard.html",
                  context={"loggedin": request.user.is_authenticated})

def ajax_new_user(request):
    user_first_name = request.POST.get('user_first_name')
    user_last_name = request.POST.get('user_last_name')
    user_email = request.POST.get('user_email')
    user_password = request.POST.get('user_password')

    # Check if user email is already signed up if so return error
    if User.objects.filter(username=user_email).exists():
        response = JsonResponse({"error": "An account with this email already exist!"}, status=400)
        return response

    new_user = User.objects.create_user(username=user_email, email=user_email, password=user_password, first_name=user_first_name,
                                         last_name=user_last_name)
    new_user.save()

    return JsonResponse({})

def ajax_user_login(request):
    print("RUNNING");
    user_email = request.GET.get('user_email')
    user_password = request.GET.get('user_password')

    user_authenticated = authenticate(request, username=user_email, password=user_password)
    login(request, user_authenticated)

    if not user_authenticated.is_authenticated:
        # Need to fix status codes
        response = JsonResponse({"error": "Username or password is incorrect"}, status=401)
        return response

    return JsonResponse({})


def user_logout(request):
    logout(request)
    return redirect('/login/')

