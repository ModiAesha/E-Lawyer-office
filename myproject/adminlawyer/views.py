from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
# from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from adminlawyer.models import *


import os
# import mysql.connector


def layout(request):
	context = {}
	return render(request,'adminlawyer/layout.html',context)

def profile(request):
	context = {}
	return render(request,'adminlawyer/profile.html',context)

def header(request):
	context = {}
	return render(request,'adminlawyer/header.html',context)

def sidebar(request):
	context = {}
	return render(request,'adminlawyer/sidebar.html',context)

def footer(request):
	context = {}
	return render(request,'adminlawyer/footer.html',context)

def dashboard(request):
	context = {}
	return render(request,'adminlawyer/dashboard.html',context)

def table(request):
	context = {}
	return render(request,'adminlawyer/table.html',context)

def form(request):
	context = {}
	return render(request,'adminlawyer/form.html',context)

def calendar(request):
	context = {}
	return render(request,'adminlawyer/calendar.html',context)

def add_case(request):
	result = Client.objects.all()
	result1 = Lawyer.objects.all()
	context = {'result':result,'result1':result1}
	return render(request,'adminlawyer/add_case.html',context)

def add_client(request):
	context = {}
	return render(request,'adminlawyer/add_client.html',context)

def add_doc(request):
	context = {}
	return render(request,'adminlawyer/add_doc.html',context)

def add_member(request):
	context = {}
	return render(request,'adminlawyer/add_member.html',context)

def view_cases(request):
	result = Cases.objects.all()
	context = {'result':result}
	return render(request,'adminlawyer/view_cases.html',context)

def view_client(request):
	result = Client.objects.all()
	context = {'result':result}
	return render(request, 'adminlawyer/view_client.html',context)

def view_doc(request):
	context = {}
	return render(request,'adminlawyer/view_doc.html',context)

def view_member(request):
	result = Lawyer.objects.all()
	context = {'result':result}
	return render(request,'adminlawyer/view_member.html',context)

def view_feedback(request):
	context = {}
	return render(request,'adminlawyer/view_feedback.html',context)

def view_appointment(request):
	context = {}
	return render(request,'adminlawyer/view_appointment.html',context)
	
def login(request):
	context = {}
	return render(request,'adminlawyer/login.html',context)


def lawyer_store(request):
	username    = request.POST['username']
	email = request.POST['email']
	lawyer_name = request.POST['lawyer_name']
	password = request.POST['password']
	dob = request.POST['dob']
	age = 20
	gender = request.POST['gender']
	contact = request.POST['contact']
	qualification = request.POST['qualification']
	experience = request.POST['experience']
	registration_date = request.POST['registration_date']
	address = request.POST['address']
	city = request.POST['city']
	state = request.POST['state']
	zipcode = request.POST['zipcode']
	photo = request.FILES['photo']
	mylocation = os.path.join(settings.MEDIA_ROOT, 'staff')
	obj = FileSystemStorage(location=mylocation)
	obj.save(photo.name, photo)

	result = User.objects.create_user(email=email,username=username,password=password)
	Lawyer.objects.create(qualification = qualification, experience = experience, registration_date = registration_date, photo = photo.name, username = username, lawyer_name = lawyer_name, email = email, address = address, contact = contact, password = password, dob = dob, age = age, gender = gender, city_id = city, state_id = state, zipcode = zipcode,user_id=result.id)
	return redirect('/adminlawyer/add_member')

def login_check(request):
    username = request.POST['username']
    password = request.POST['password']

    result = auth.authenticate(request, username=username, password=password)

    if result is None:
        print('Invalid Username Or Password')
        return redirect('/adminlawyer/login')
    else:
        auth.login(request, result)
        return redirect('/adminlawyer/dashboard')


def logout(request):
    auth.logout(request)
    return redirect('/adminlawyer/login')


def client_store(request):
	username    = request.POST['username']
	email = request.POST['email']
	client_name = request.POST['client_name']
	password = request.POST['password']
	dob = request.POST['dob']
	age = 20
	gender = request.POST['gender']
	contact = request.POST['contact']
	address = request.POST['address']
	city = request.POST['city']
	state = request.POST['state']
	zipcode = request.POST['zipcode']
	photo = request.FILES['photo']
	mylocation = os.path.join(settings.MEDIA_ROOT, 'client')
	obj = FileSystemStorage(location=mylocation)
	obj.save(photo.name, photo)

	result = User.objects.create_user(email=email,username=username,password=password)
	Client.objects.create(photo = photo.name, username = username, client_name = client_name, email = email, address = address, contact = contact, password = password, dob = dob, age = age, gender = gender, city_id = city, state_id = state, zipcode = zipcode,user_id=result.id)
	return redirect('/adminlawyer/add_client')


def client_update(request,id):
	photo = request.FILES['p']
	mylocation = os.path.join(settings.MEDIA_ROOT, 'client')
	obj = FileSystemStorage(location=mylocation)
	obj.save(photo.name, photo)

	data = {
				'photo' : photo.name,
				'client_name'        : request.POST['client_name'],
				'username'        : request.POST['username'],
				'email'       : request.POST['email'],
				'password'       : request.POST['password'],
				'dob'       : request.POST['dob'],
				'age' : 20,
				'gender'       : request.POST['gender'],
				'address'      : request.POST['address'],
				'contact' : request.POST['contact'],
				'city_id'     : request.POST['city'],
				'state_id' 		   : request.POST['state'],
				'zipcode'     : request.POST['zipcode'],
				
		   }
	Client.objects.update_or_create(pk=id, defaults=data)
	return redirect('/adminlawyer/view_client')


def lawyer_update(request,id):
	photo = request.FILES['photo']
	mylocation = os.path.join(settings.MEDIA_ROOT, 'client')
	obj = FileSystemStorage(location=mylocation)
	obj.save(photo.name, photo)

	data = {
				'photo' : photo.name,
				'lawyer_name'        : request.POST['lawyer_name'],
				'username'        : request.POST['username'],
				'email'       : request.POST['email'],
				'password'       : request.POST['password'],
				'dob'       : request.POST['dob'],
				'age' : 20,
				'gender'       : request.POST['gender'],
				'qualification'       : request.POST['qualification'],
				'experience'       : request.POST['experience'],
				'registration_date'       : request.POST['registration_date'],
				'address'      : request.POST['address'],
				'contact' : request.POST['contact'],
				'city_id'     : request.POST['city'],
				'state_id' 		   : request.POST['state'],
				'zipcode'     : request.POST['zipcode'],
				
		   }
	Lawyer.objects.update_or_create(pk=id, defaults=data)
	return redirect('/adminlawyer/view_member')


def case_store(request):
	title    = request.POST['title']
	description = request.POST['description']
	police_station = request.POST['police_station']
	case_type = request.POST['case_type']
	case_reg_date = request.POST['case_reg_date']
	court = request.POST['court']
	judge = request.POST['judge']
	status = request.POST['status']
	city = request.POST['city']
	state = request.POST['state']
	client = request.POST['client']
	lawyer = request.POST['lawyer']
	fir_copy = request.FILES['fir_copy']
	mylocation = os.path.join(settings.MEDIA_ROOT, 'client')
	obj = FileSystemStorage(location=mylocation)
	obj.save(fir_copy.name, fir_copy)

	Cases.objects.create(fir_copy = fir_copy.name, title = title, description = description, police_station = police_station, case_type = case_type, case_reg_date = case_reg_date, court = court, judge = judge, status = status, client_id = client, lawyer_id = lawyer, city_id = city, state_id = state)
	return redirect('/adminlawyer/add_case')



def case_update(request,id):
	fir_copy = request.FILES['fir_copy']
	mylocation = os.path.join(settings.MEDIA_ROOT, 'client')
	obj = FileSystemStorage(location=mylocation)
	obj.save(fir_copy.name, fir_copy)

	data = {
				'title'        : request.POST['title'],
				'description'       : request.POST['description'],
				'police_station'      : request.POST['police_station'],
				'case_type' : request.POST['case_type'],
				'case_reg_date'     : request.POST['case_reg_date'],
				'court' 		   : request.POST['court'],
				'judge'     : request.POST['judge'],
				'status'     : request.POST['status'],
				'city_id'     : request.POST['city'],
				'state_id'     : request.POST['state'],
				'client_id'     : request.POST['client'],
				'lawyer_id'     : request.POST['lawyer'],
				'fir_copy'     : fir_copy.name,
		   }
	Cases.objects.update_or_create(pk=id, defaults=data)
	return redirect('/adminlawyer/view_cases')

def view(request):
	pass


def client_delete(request,id):
	result = Client.objects.get(pk=id)
	result.delete()
	return redirect('/adminlawyer/view_client')


def lawyer_delete(request,id):
	result = Lawyer.objects.get(pk=id)
	result.delete()
	return redirect('/adminlawyer/view_member')


def case_delete(request,id):
	result = Cases.objects.get(pk=id)
	result.delete()
	return redirect('/adminlawyer/view_cases')


def client_edit(request,id):
	result  = Client.objects.get(pk=id)
	city = City.objects.all()
	state = State.objects.all()
	context = {'result':result,'city':city,'state':state}
	return render(request, 'adminlawyer/update_client.html',context)


def lawyer_edit(request,id):
	result  = Lawyer.objects.get(pk=id)
	city = City.objects.all()
	state = State.objects.all()
	context = {'result':result,'city':city,'state':state}
	return render(request, 'adminlawyer/update_member.html',context)


def case_edit(request,id):
	result  = Cases.objects.get(pk=id)
	lawyer = Lawyer.objects.all()
	client = Client.objects.all()
	city = City.objects.all()
	state = State.objects.all()
	context = {'result':result,'city':city,'state':state,'lawyer':lawyer,'client':client}
	return render(request, 'adminlawyer/update_case.html',context)













# connector

	# try:
	#     connection = mysql.connector.connect(host='localhost',
	#                                          database='lawyeroffice',
	#                                          user='root',
	#                                          password='')

	#     sql_select_Query = "select * from client where id=3"
	#     cursor = connection.cursor()
	#     cursor.execute(sql_select_Query)
	#     # get all records
	#     records = cursor.fetchall()
	#     print("Total number of rows in table: ", cursor.rowcount)

	#     # print("\nPrinting each row")
	#     for row in records:
	#         print("Id = ", row[0], )
	#         print("Name = ", row[1])
	#         # print("Price  = ", row[2])
	#         # print("Purchase date  = ", row[3], "\n")

	# except mysql.connector.Error as e:
	#     print("Error reading data from MySQL table", e)
	# finally:
	#     if connection.is_connected():
	#         connection.close()
	#         cursor.close()
	#         print("MySQL connection is closed")