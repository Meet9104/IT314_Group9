from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
# Create your views here.
from pymongo import MongoClient
client = MongoClient(
    'mongodb+srv://maharth:maharth@cluster0.xsqej9v.mongodb.net/test')
db = client['Leave_Management_System']


def profile_page(request):

    facultytable = db['faculty info']
    reply = facultytable.find_one({'email': request.session.get('username')})

    if reply is None:
        studenttable = db['student info']
        reply = studenttable.find_one(
            {'email': request.session.get('username')})

    if reply is None:
        tatble = db['ta info']
        reply = tatble.find_one({'email': request.session.get('username')})

    if reply is None:
        adminTablte = db['adminTable']
        reply = adminTablte.find_one(
            {'email': request.session.get('username')})

    if reply:
        context = {
            'user': reply,
        }
        return render(request, 'profile.html', context)


def logout_view(request):
    request.session['username'] = None
    messages.success(request, "You have been logged out successfully!")
    return redirect('index')


def index(request):
    if request.session.get('username'):

        adminTable = db['adminTable']
        reply = adminTable.find_one({'email': request.session.get('username')})

        if reply:
            context = {
                'user': reply,
            }
            return render(request, 'admin_page.html', context)

        facultytable = db['faculty info']
        reply = facultytable.find_one(
            {'email': request.session.get('username')})

        if reply:
            context = {
                'user': reply,
            }
            return render(request, 'faculty.html', context)

        studenttable = db['student info']
        reply = studenttable.find_one(
            {'email': request.session.get('username')})

        if reply:
            context = {
                'user': reply,
            }
            return render(request, 'student.html', context)

        tatble = db['ta info']
        reply = tatble.find_one({'email': request.session.get('username')})

        if reply:
            context = {
                'user': reply,
            }
            return render(request, 'ta.html', context)

    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            adminTable = db['adminTable']
            reply = adminTable.find_one({'email': username})
            if reply:
                if reply['password'] == password:
                    request.session['username'] = username
                    messages.success(
                        request, "You have been logged in successfully as admin!")
                    return render(request, 'admin_page.html', {'user': reply})

            studenttable = db['student info']
            reply = studenttable.find_one({'email': username})

            if reply:
                if reply['password'] == password:
                    request.session['username'] = username
                    messages.success(
                        request, "You have been logged in successfully as Student!")
                    return render(request, 'student.html', {'user': reply})

            facultytable = db['faculty info']
            reply = facultytable.find_one({'email': username})

            if reply:
                if reply['password'] == password:
                    request.session['username'] = username
                    messages.success(
                        request, "You have been logged in successfully as Faculty!")
                    return render(request, 'faculty.html', {'user': reply})

            tatble = db['ta info']
            reply = tatble.find_one({'email': username})

            if reply:
                if reply['password'] == password:
                    request.session['username'] = username
                    messages.success(
                        request, "You have been logged in successfully as TA!")
                    return render(request, 'ta.html', {'user': reply})

            messages.error(request, "Please Enter Valid Details!")
            return render(request, 'index.html', {'form': form, 'msg': msg})

    return render(request, 'index.html', {'form': form, 'msg': msg})


def leaveform(request):
    if request.session.get('username'):

        facultytable = db['faculty info']
        reply = facultytable.find_one(
            {'email': request.session.get('username')})

        if reply:
            context = {
                'user': reply,
            }
            return render(request, 'leaveform.html', context)

        studenttable = db['student info']
        reply = studenttable.find_one(
            {'email': request.session.get('username')})

        if reply:
            context = {
                'user': reply,
            }
            return render(request, 'leaveform.html', context)

        tatble = db['ta info']
        reply = tatble.find_one({'email': request.session.get('username')})

        if reply:
            context = {
                'user': reply,
            }
            return render(request, 'leaveform.html', context)


def dashboard_redirect_after_leave_apply(request):
    if request.method == 'POST':
        leave_type = request.POST.get('leave-type')
        leave_duration = request.POST.get('leave-duration')
        from_date = request.POST.get('from-date')
        to_date = request.POST.get('to-date')
        reason = request.POST.get('reason')

        if from_date > to_date:
            messages.error(request, 'From date cannot be greater than to date')
            return render(request, 'leaveform.html')

        username = request.session.get('username')

        studenttable = db['student info']
        reply = studenttable.find_one({'email': username})

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
            id = reply['id']

        facultytable = db['faculty info']
        reply = facultytable.find_one({'email': username})

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
            id = reply['id']

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
            id = reply['id']

        leaveTableEntry = {
            'leave_type': leave_type,
            'leave_duration': leave_duration,
            'from_date': from_date,
            'to_date': to_date,
            'reason': reason,
            'emailList': emailList,
            'status': 'pending',
            'role': role,
            'name': name,
            'email': email,
            'id': id,
        }

        if len(from_date) == 0 or len(to_date) == 0 or len(reason) == 0:
            messages.error(
                request, "Please fill all the details before submitting!")
            return render(request, 'leaveform.html')

        leaveTable = db['leaveTable']
        leaveTable.insert_one(leaveTableEntry)

        if leaveTableEntry is not None:
            messages.success(
                request, "You have successfully applied for leave!")
        else:
            messages.error(request, "Error in applying for leave!")

    if request.session.get('username'):

        facultytable = db['faculty info']
        reply = facultytable.find_one(
            {'email': request.session.get('username')})

        if reply:
            context = {
                'user': reply,
            }
            return render(request, 'faculty.html', context)

        studenttable = db['student info']
        reply = studenttable.find_one(
            {'email': request.session.get('username')})

        if reply:
            context = {
                'user': reply,
            }
            return render(request, 'student.html', context)

        tatble = db['ta info']
        reply = tatble.find_one({'email': request.session.get('username')})

        if reply:
            context = {
                'user': reply,
            }
            return render(request, 'ta.html', context)

            # if reply is None:
        adminTablte = db['adminTable']
        reply = adminTablte.find_one(
            {'email': request.session.get('username')})

        if reply:
            context = {
                'user': reply,
            }
            return render(request, 'admin_page.html', context)


def admin_page(request):
    if request.session.get('username'):
        adminTablte = db['adminTable']
        reply = adminTablte.find_one(
            {'email': request.session.get('username')})
        if reply:
            context = {
                'user': reply,
            }
        return render(request, 'admin_page.html', context)


def leave_status_approved(request):
    if request.session.get('username'):
        leaveTable = db['leaveTable']
        # reply = adminTablte.find_one({'email': request.session.get('username')})
        # print()
        # reply = leaveTable.find_one({'status': 'approved'})
        # print(reply)
        reply = leaveTable.find()
        return render(request, 'leave_status_approved.html', {'reply': reply})


def leave_status_pending(request):
    if request.session.get('username'):
        leaveTable = db['leaveTable']
        # reply = adminTablte.find_one({'email': request.session.get('username')})
        # reply = leaveTable.find_one({'status': 'pending'})
        # if reply:
        #     context = {
        #         'user': reply,
        #     }

        
        reply = leaveTable.find()
        return render(request, 'leave_status_pending.html', {'reply': reply})


def leave_status_rejected(request):
    if request.session.get('username'):
        leaveTable = db['leaveTable']
        # reply = adminTablte.find_one({'email': request.session.get('username')})
        # reply = leaveTable.find_one({'status': 'rejected'})
        # if reply:
        #     context = {
        #         'user': reply,
        #     }
        reply = leaveTable.find()
        print(reply)
        return render(request, 'leave_status_rejected.html', {'reply': reply})
    

