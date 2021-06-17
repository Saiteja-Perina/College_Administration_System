from django.db import models

# Create your models here.
class Department(models.Model):
	dept_name=models.CharField(max_length=25,primary_key=True)
	total_faculty=models.IntegerField()

	def __str__(self):
		return self.dept_name

	class Meta:
		db_table="Department"

class Faculty(models.Model):
	faculty_id=models.CharField(max_length=10,primary_key=True)
	fac_name=models.CharField(max_length=50)
	fac_user_name=models.CharField(max_length=50)
	fac_password=models.CharField(max_length=25)
	fac_dept=models.ForeignKey(Department,on_delete=models.CASCADE)

	def __str__(self):
		return self.fac_user_name

	class Meta:
		db_table="Faculty"

class Subject(models.Model):
	subject_br_id=models.CharField(max_length=10,primary_key=True)
	sub_name=models.CharField(max_length=50)
	sub_branch=models.ForeignKey(Department,on_delete=models.CASCADE)
	sem_no=models.IntegerField()

	def __str__(self):
		return self.sub_name

	class Meta:
		db_table="Subject"

class Teaches(models.Model):
	t_id=models.AutoField(primary_key=True)
	f_id=models.ForeignKey(Faculty,on_delete=models.CASCADE)
	sub_br_id=models.ForeignKey(Subject,on_delete=models.CASCADE)

	class Meta:
		db_table="Teaches"
		unique_together=(('f_id','sub_br_id'),)

class Student(models.Model):
	student_id=models.CharField(max_length=10,primary_key=True)
	stu_name=models.CharField(max_length=50)
	stu_user_name=models.CharField(max_length=50)
	stu_password=models.CharField(max_length=25)
	stu_dept=models.ForeignKey(Department,on_delete=models.CASCADE)
	stu_feebalance=models.IntegerField()

	def __str__(self):
		return self.stu_user_name

	class Meta:
		db_table="Student"

class SemAttendance(models.Model):
	att_id=models.AutoField(primary_key=True)
	sem=models.IntegerField()
	branch=models.ForeignKey(Department,on_delete=models.CASCADE)
	stud_id=models.ForeignKey(Student,on_delete=models.CASCADE)
	sub_br_id=models.ForeignKey(Subject,on_delete=models.CASCADE)
	sub_tot_attendance=models.IntegerField(default=0)
	sub_tot_present=models.IntegerField(default=0)

	class Meta:
		db_table="SemAttendance"
		unique_together=(('stud_id','sub_br_id'),)

class Internals(models.Model):
	internal_id=models.AutoField(primary_key=True)
	sem=models.IntegerField()
	branch=models.ForeignKey(Department,on_delete=models.CASCADE)
	stud_id=models.ForeignKey(Student,on_delete=models.CASCADE)
	sub_br_id=models.ForeignKey(Subject,on_delete=models.CASCADE)
	sub_tot_marks=models.IntegerField(default=25)
	sub_secured=models.IntegerField(default=0)

	class Meta:
		db_table="Internals"
		unique_together=(('stud_id','sub_br_id'),) 