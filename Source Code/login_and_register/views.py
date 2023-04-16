from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
# Create your views here.
from pymongo import MongoClient
client = MongoClient('mongodb+srv://maharth:maharth@cluster0.xsqej9v.mongodb.net/test')
db = client['Leave_Management_System']

def logout_view(request):
    request.session['username'] = None
    return redirect('index')

def index(request):
    if request.session.get('username'):
        
        facultytable = db['faculty info']
        reply = facultytable.find_one({'email': request.session.get('username')})
        # print(reply)

        if reply:
            context = {
                'user' : reply,
            }
            return render(request, 'faculty.html' , context)

        studenttable = db['student info']
        reply = studenttable.find_one({'email': request.session.get('username')})
        # print(reply)

        if reply:   
            context = {
                'user' : reply,
            }
            return render(request, 'student.html',context)

        tatble = db['ta info']
        reply = tatble.find_one({'email': request.session.get('username')})
        # print(reply)

        if reply:
            context = {
                'user' : reply,
            }
            return render(request, 'ta.html', context)
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
                    request.session['username'] = username
                    messages.success(request,"You have been logged in successfully as Student!")
                    return render(request, 'student.html', {'user' : reply})
                
            facultytable = db['faculty info']
            reply = facultytable.find_one({'email': username})
            # print(reply)
            if reply:
                if reply['password'] == password:
                    request.session['username'] = username
                    messages.success(request,"You have been logged in successfully as Faculty!")
                    return render(request, 'faculty.html', {'user' : reply})
                
            tatble = db['ta info']
            reply = tatble.find_one({'email': username})
            # print(reply)
            if reply:
                if reply['password'] == password:
                    request.session['username'] = username
                    messages.success(request,"You have been logged in successfully as TA!")
                    return render(request, 'ta.html', {'user' : reply})
            
            messages.error(request,"Please Enter Valid Details!")
            return render(request, 'index.html', {'form': form, 'msg': msg})
        
    return render(request, 'index.html', {'form': form, 'msg': msg})


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
    print(request.session.get('username'))
    if request.session.get('username'):
        
        facultytable = db['faculty info']
        reply = facultytable.find_one({'email': request.session.get('username')})
        # print(reply)

        if reply:
            context = {
                'user' : reply,
            }
            return render(request, 'faculty.html' , context)

        studenttable = db['student info']
        reply = studenttable.find_one({'email': request.session.get('username')})
        # print(reply)

        if reply:   
            context = {
                'user' : reply,
            }
            return render(request, 'student.html',context)

        tatble = db['ta info']
        reply = tatble.find_one({'email': request.session.get('username')})
        # print(reply)

        if reply:
            context = {
                'user' : reply,
            }
            return render(request, 'ta.html', context)

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
                    request.session['username'] = username
                    return render(request, 'student.html', {'user' : reply})
                
            facultytable = db['faculty info']
            reply = facultytable.find_one({'email': username})
            # print(reply)
            if reply:
                if reply['password'] == password:
                    request.session['username'] = username
                    return render(request, 'faculty.html', {'user' : reply})
                
            tatble = db['ta info']
            reply = tatble.find_one({'email': username})
            # print(reply)
            if reply:
                if reply['password'] == password:
                    request.session['username'] = username
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

def leaveform(request):
    if request.session.get('username'):
        
        facultytable = db['faculty info']
        reply = facultytable.find_one({'email': request.session.get('username')})
        # print(reply)

        if reply:
            context = {
                'user' : reply,
            }
            return render(request, 'leaveform.html' , context)

        studenttable = db['student info']
        reply = studenttable.find_one({'email': request.session.get('username')})
        # print(reply)

        if reply:   
            context = {
                'user' : reply,
            }
            return render(request, 'leaveform.html',context)

        tatble = db['ta info']
        reply = tatble.find_one({'email': request.session.get('username')})
        # print(reply)

        if reply:
            context = {
                'user' : reply,
            }
            return render(request, 'leaveform.html', context)
    # return render(request,'leaveform.html')

def dashboard_redirect_after_leave_apply(request):
    if request.method == 'POST':
        leave_type = request.POST.get('leave-type')
        leave_duration = request.POST.get('leave-duration')
        from_date = request.POST.get('from-date')
        to_date = request.POST.get('to-date')
        reason = request.POST.get('reason')
        # semester = request.POST.get('semester')
        # reason = request.POST.get('reason')
        # date = request.POST.get('date')
        # print(name,email,rollno,department,year,semester,reason,date)
        # print(leave_type,leave_duration,from_date,to_date,reason)
        # studenttable = db['student info']
        username = request.session.get('username')
        
        studenttable = db['student info']
        reply = studenttable.find_one({'email': username})
        # print(reply)
        
        if reply:
            emailList = []
            emailList.append(username)
            for i in reply['faculties']:
                emailList.append(i)

            for i in reply['tas']:
                emailList.append(i)
            role = "student"
            name = reply['name']
            email = reply['email']
            print(emailList)
            
            print(reply)
            
        facultytable = db['faculty info']
        reply = facultytable.find_one({'email': username})
        # print(reply)
        
        if reply:
            emailList = []
            emailList.append(username)
            for i in reply['faculties']:
                emailList.append(i)

            for i in reply['tas']:
                emailList.append(i)
            role = "faculty"
            name = reply['name']
            email = reply['email']
            print(emailList)
            
            print(reply)
        # if reply:
        #     print(reply)
            
        tatble = db['ta info']
        reply = tatble.find_one({'email': username})
        
        if reply:
            emailList = []
            emailList.append(username)
            for i in reply['faculties']:
                emailList.append(i)

            for i in reply['tas']:
                emailList.append(i)
            role = "ta"
            name = reply['name']
            email = reply['email']
            print(emailList)
            
            print(reply)
        # # print(reply)
        # if reply:
        #     print(reply)

         
        
        leaveTableEntry = {
            'leave_type': leave_type,
            'leave_duration': leave_duration,
            'from_date': from_date,
            'to_date': to_date,
            'reason': reason,
            'emailList': emailList,
            'status': 'pending',    
            'role': role,
            # 'name' : reply['name'],
            # 'email' : reply['email'],
            'name' : name,
            'email' : email,
            


        }
        leaveTable = db['leaveTable']
        leaveTable.insert_one(leaveTableEntry)
        
        # studenttable.insert_one({'name': name, 'email': email, 'rollno': rollno, 'department': department, 'year': year, 'semester': semester, 'reason': reason, 'date': date})
        # if (role=="student"):
        #     return render(request,'student.html') 
        # elif (role=="faculty"):
        #     return render(request,'faculty.html')
        # elif (role=="ta"):
        #     return render(request,'ta.html')
        # return render(request,'student.html')
    if request.session.get('username'):
        
        facultytable = db['faculty info']
        reply = facultytable.find_one({'email': request.session.get('username')})
        # print(reply)

        if reply:
            context = {
                'user' : reply,
            }
            return render(request, 'faculty.html' , context)

        studenttable = db['student info']
        reply = studenttable.find_one({'email': request.session.get('username')})
        # print(reply)

        if reply:   
            context = {
                'user' : reply,
            }
            return render(request, 'student.html',context)

        tatble = db['ta info']
        reply = tatble.find_one({'email': request.session.get('username')})
        # print(reply)

        if reply:
            context = {
                'user' : reply,
            }
            return render(request, 'ta.html', context)
    # return render(request,'student.html')