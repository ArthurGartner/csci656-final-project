from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.contrib.auth.models import User
import json
# Create your views here.


def page_index(request):
    return render(request=request,
                  template_name="main/page_index.html")


def page_about(request):
    return render(request=request,
                  template_name="main/page_about.html")


def page_checklist(request):
    return render(request=request,
                  template_name="main/page_checklist.html")


def page_future_work(request):
    return render(request=request,
                  template_name="main/page_future_work.html")


def page_login(request):
    return render(request=request,
                  template_name="main/page_login.html")


def page_signup(request):
    return render(request=request,
                  template_name="main/page_signup.html")


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

    page_login(request)

    return JsonResponse({})


