from django.shortcuts import render
from django.http import HttpResponse

member = [
    {
        'name': 'Kwizera',
        'position': 'security'
    },
        {
        'name': 'Kwizera OG',
        'position': 'security'
    }
]

def say_hello(request):
    return render(request, 'index.html',{'name':'Nahayo'})
def team_view(request):
    context = {
        'member': member
    }
    return render(request, 'posts/team.html', context)