from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def courses(request):
    return HttpResponse('''
                        <h1>This is courses page</h1>
                        <h1> <a href='/secondapp/feedback/'>feedback</a> </h1>
                        <h1><a href='/firstapp/about/'>About</a></h1>
                        <h1> <a href='/firstapp/contact/'>Contact</a> </h1>
                        ''')

def feedback(request):
    return HttpResponse('''
                        <h1>This is feedback page</h1>
                        <h1> <a href='/secondapp/courses/'>courses</a> </h1>
                        <h1><a href='/firstapp/about/'>About</a></h1>
                        <h1> <a href='/firstapp/contact/'>Contact</a> </h1>
                        ''')
