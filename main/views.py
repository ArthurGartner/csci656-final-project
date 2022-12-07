import os

from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect
from main.models import *
import boto3
import json
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
    lambda_call()
    return render(request=request,
                  template_name="main/page_signup.html",
                  context={"loggedin": request.user.is_authenticated})

def page_job_dashboard(request):
    if not request.user.is_authenticated:
        return page_login(request)

    # user_job_events = Event.objects.filter(job_app__user=request.user).group_by('')

    # user_job_events = Event.objects.filter(job_app__user=request.user).order_by()

    user_job_events = []

    all_events = Event.objects.filter(job_app__user=request.user).order_by('-event_date')

    user_job_apps = JobApp.objects.filter(user=request.user)

    # Needs to be re-written using better queries. Will not scale well
    for user_app in user_job_apps:
        user_job_events.append(Event.objects.filter(job_app=user_app).order_by('-event_date')[0])

    return render(request=request,
                  template_name="main/page_jobs_dashboard.html",
                  context={"loggedin": request.user.is_authenticated,
                           "events": user_job_events,
                           "all_events": all_events})

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
    user_email = request.GET.get('user_email')
    user_password = request.GET.get('user_password')

    user_authenticated = authenticate(request, username=user_email, password=user_password)
    login(request, user_authenticated)

    if not user_authenticated.is_authenticated:
        # Need to fix status codes
        response = JsonResponse({"error": "Username or password is incorrect"}, status=401)
        return response

    return JsonResponse({})

def ajax_save_job(request):
    job_name = request.POST.get('job_name')
    company_name = request.POST.get('company_name')
    position_url = request.POST.get('position_url')
    event_select = request.POST.get('event_select')
    event_date = request.POST.get('event_date')
    personal_position_notes = request.POST.get('personal_position_notes')
    public_position_notes = request.POST.get('public_position_notes')

    company, created = Company.objects.get_or_create(company_name=company_name)

    job = Job(position_name=job_name, position_url=position_url, company=company)
    job.save()

    job_app = JobApp(user=request.user, job=job)
    job_app.save()

    event = Event(event_type=event_select, event_date=event_date, personal_notes=personal_position_notes,
                  public_notes=public_position_notes, job_app=job_app)
    event.save()

    return JsonResponse({})

def ajax_save_event(request):
    event_select = request.POST.get('event_select')
    event_date = request.POST.get('event_date')
    job_app_id = request.POST.get('job_app_id')

    job_app = JobApp.objects.filter(id=job_app_id)[0]

    Event(event_type=event_select, event_date=event_date, job_app=job_app).save()

    return JsonResponse({})

def ajax_delete_job(request):
    job_app_id = request.GET.get('job_app_id')
    JobApp.objects.get(id=job_app_id).delete()
    return JsonResponse({})

def ajax_refresh_job_list(request):
    user_job_events = []

    all_events = Event.objects.filter(job_app__user=request.user).order_by('-event_date')

    user_job_apps = JobApp.objects.filter(user=request.user)

    # Needs to be re-written using better queries. Will not scale well
    for user_app in user_job_apps:
        user_job_events.append(Event.objects.filter(job_app=user_app).order_by('-event_date')[0])

    return render(request=request,
                  template_name="main/jobs_list.html",
                  context={"loggedin": request.user.is_authenticated,
                           "events": user_job_events,
                           "all_events": all_events})


def user_logout(request):
    logout(request)
    return redirect('/login/')

def lambda_call():
    lambda_client = boto3.client('lambda', os.environ.get('AWS_DEFAULT_REGION'))

    urls_to_check = 'https://google.com'
    data = {
        "urls":["https://google.com", "https://facebook.com"]
    }

    response = lambda_client.invoke(
        FunctionName='jobjump_url_check',
        Payload=json.dumps(data),
    )

    print(response['Payload'])
    print(response['Payload'].read().decode("utf-8"))