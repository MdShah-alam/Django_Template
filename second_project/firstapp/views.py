from django.shortcuts import render
from django.http import HttpResponse

def contact(request):
    return HttpResponse('''
                        <h1>This is contact page </h1>
                        <h1><a href='/firstapp/about/'>About</a></h1>
                        <h1> <a href='/secondapp/feedback/'>feedback</a> </h1>
                        <h1> <a href='/secondapp/courses/'>courses</a> </h1>
                        ''')

def abuot(request):
    return HttpResponse('''
                        <h1>This is about page </h1>
                        <h1> <a href='/firstapp/contact/'>Contact</a> </h1>
                        <h1> <a href='/secondapp/feedback/'>feedback</a> </h1>
                        <h1> <a href='/secondapp/courses/'>courses</a> </h1>
                        ''')
