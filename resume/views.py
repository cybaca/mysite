from django.shortcuts import render

def ResumeView(request):
    context = None
    return render(request, 'resume/resume.html', context)
