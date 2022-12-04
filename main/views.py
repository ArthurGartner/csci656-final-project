from django.shortcuts import render

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


