from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
# Create your views here.

def register(request):

    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        username = request.POST['uname']
        pwd1 = request.POST['pwd']
        pwd2 = request.POST['cpwd']
        email = request.POST['email']


        user = User.objects.create_user(username=username, password=pwd1, email=email, first_name=first_name, last_name=last_name)
        user.save()
        print('User created')
        return redirect('/')
    else:
        return render(request, 'register.html')
