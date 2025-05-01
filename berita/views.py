from django.shortcuts import render

# Create your views here.

def dashboard(requset):
    template_name = "dashboard/index.html"
    context = {
        'title' : 'halaman dashboard'
    }
    return render(requset, template_name, context)