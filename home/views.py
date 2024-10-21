from django.shortcuts import render

def HomeView(request):
    context = None
    return render(request, 'home/home.html', context)
