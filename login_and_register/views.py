from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
# Create your views here.
from pymongo import MongoClient
client = MongoClient('mongodb+srv://maharth:maharth@cluster0.xsqej9v.mongodb.net/test')
db = client['Leave_Management_System']


def index(request):
    return render(request, 'index.html')


def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # print(username, password)

            studenttable = db['student info']
            reply = studenttable.find_one({'email': username})
            # print(reply)
            if reply:
                if reply['password'] == password:
                    return render(request, 'student.html', {'user' : reply})
                
            facultytable = db['faculty info']
            reply = facultytable.find_one({'email': username})
            # print(reply)
            if reply:
                if reply['password'] == password:
                    return render(request, 'faculty.html', {'user' : reply})
                
            tatble = db['ta info']
            reply = tatble.find_one({'email': username})
            # print(reply)
            if reply:
                if reply['password'] == password:
                    return render(request, 'ta.html', {'user' : reply})
    return render(request, 'login.html', {'form': form, 'msg': msg})

            # return redirect('student.html')
            # print(reply)
        #     user = authenticate(username=username, password=password)
        #     if user is not None and user.is_faculty:
        #         login(request, user)
        #         return redirect('facultypage')
        #     elif user is not None and user.is_ta:
        #         login(request, user)
        #         return redirect('ta')
        #     elif user is not None and user.is_student:
        #         login(request, user)
        #         return redirect('student')
        #     else:
        #         msg= 'invalid credentials'
        # else:
        #     msg = 'error validating form'
  

# def faculty(request):
#     return render(request,'faculty.html')


# def ta(request):
#     return render(request,'ta.html')


# def student(request):
#     return render(request,'student.html')