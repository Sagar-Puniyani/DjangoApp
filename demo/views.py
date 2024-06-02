from django.shortcuts import render

# Create your views here.
def some_demo(request):
    return render(request , 'demo/demo.html')

