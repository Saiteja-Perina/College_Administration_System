from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
# Create your views here.
def center(request):
	return render(request,'home.html')

def faclog(re): 
	if re.method=='POST':
		uname=re.POST['uname']
		psw=re.POST['psw']
		try:
			data=Faculty.objects.get(fac_user_name=uname,fac_password=psw)
			return render(re,'facultyduties.html',{'data':data})
		except:
			l="<html><head><title>Invalid</title></head><body><h1 style='color:#fa5432; text-align:center'>Invalid Login</h1></body></html>"
			return HttpResponse(l)
	return render(re,'faclog.html')

def studlog(r):
	if r.method=='POST':
		uname=r.POST['uname']
		psw=r.POST['psw']
		try:
			data=Student.objects.get(stu_user_name=uname,stu_password=psw)
			return render(r,'studentservices.html',{'data':data})
		except:
			l="<html><head><title>Invalid</title></head><body><h1 style='color:#2345af; text-align:center'>Invalid Login</h1></body></html>"
			return HttpResponse(l)
	return render(r,'studlog.html')

def feecheck(request,id):
	data=Student.objects.get(student_id=id)
	return render(request,'feecheck.html',{'data':data})

def choose(req,id):
	data=Teaches.objects.filter(f_id=id)
	return render(req,'choose.html',{'data':data})

def choose1(req,id):
	data=Teaches.objects.filter(f_id=id)
	return render(req,'choose1.html',{'data':data})

def markattend(r,id):
	data=SemAttendance.objects.filter(sub_br_id_id=id)
	if r.method=='POST':
		for i in data:
			i.sub_tot_attendance+=1
			val=r.POST[i.stud_id_id]
			if val=="Present":
				i.sub_tot_present+=1
			i.save()
		return render(r,'success.html')
	return render(r,'markattend.html',{'data':data})

def entermarks(r,id):
	data=Internals.objects.filter(sub_br_id_id=id)
	if r.method=='POST':
		for i in data:
			i.sub_secured=r.POST[i.stud_id_id]
			i.save()
		return render(r,'success.html')
	return render(r,'entermarks.html',{'data':data})

def attendancecheck(re,id):
	data=SemAttendance.objects.filter(stud_id_id=id)
	return render(re,'attendancecheck.html',{'data':data})

def markscheck(re,id):
	data=Internals.objects.filter(stud_id_id=id)
	return render(re,'markscheck.html',{'data':data})