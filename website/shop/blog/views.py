from django.shortcuts import render
posts=[
    {
        'author':'Sharon',
        'content':'My own Django project',
        'date':'August 24 2020'
    },
]

def home (request):
    context={
        'posts':posts
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html')
   


# Create your views here.
