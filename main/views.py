from django.shortcuts import render

# Create your views here.


def page_index(request):
    return render(request=request,
                  template_name="main/page_index.html")
