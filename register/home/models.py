from pyexpat import model
from random import choices
from tabnanny import verbose
from tkinter import OFF, ON
from unicodedata import name
from django.db import models

# Create your models here.

                                                                                                                    # FEEDBACK
#[++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++]

#Model for the Feedback of the people..
class Contact(models.Model):
    email = models.CharField(max_length=60)
    message = models.TextField(max_length=300)
    phone = models.CharField(max_length=10)
    date = models.DateField()

    def __str__(self):
        return (self.email)
    
    class Meta:
        verbose_name_plural = "Student Feedback/Contact Forms"
                                                                                                                # SUDENT REGISTRATION
#[+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++]

#Model for user registration..
class Student_Registration(models.Model):
    #choices for department and Year is made here using a tuple.
    dept_choices = (
        ('BSc', 'Bachelor of Science'),
        ('IT', 'Bachelor of Information Technology'),
        ('BTECH', 'Engineering'),
        ('MSc','Master of Science'),
        ('HUMAN','Humanities')
    )
    year_choices = (
        ('1','1st'),
        ('2','2nd'),
        ('3','3rd'),
        ('4','4th')
    )

    firstName = models.CharField(max_length=25)
    middleName = models.CharField(max_length=25,blank=True)
    lastName = models.CharField(max_length=25)
    email = models.CharField(max_length=60)
    telephone = models.CharField(max_length=10)
    rollNumber = models.CharField(max_length=15)
    date = models.DateTimeField(auto_now_add=True)
    department = models.CharField(max_length=5, choices=dept_choices)
    year = models.CharField(max_length=1, choices=year_choices)

    def __str__(self):
        return 'Name : {} {} {}  |  Rol_no :{}  |  Dept - {}  |  Year : {}'.format(self.firstName, self.middleName, self.lastName , self.rollNumber, self.department, self.year)
    class Meta:
        verbose_name_plural = "Registered Student Names"

                                                                                                            # VOTED STUDENTS LIST
#[+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++]

#model for students who have already voted  ..
class Logged(models.Model):
    email = models.CharField(max_length=60)
    details = models.ForeignKey(Student_Registration, on_delete=models.CASCADE)

    def __str__(self):
        return 'Email : {} | Details : {} '.format(self.email, self.details)

    class Meta:
        verbose_name_plural = "Voted Student List"
                                                                                                             # POSITIONS 
#[++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++]

#creating the positions table..
class Positions(models.Model):
    name = models.CharField(max_length=80)
    priority = models.IntegerField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Ballot Position List"

                                                                                                            # CANDIDATE
#[+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++]
#creating the candidates table....
class Candidate(models.Model):
    name = models.CharField(max_length=80)
    bio = models.TextField(max_length=300)
    position = models.ForeignKey(Positions, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return 'Name : {} | Postion : {} | Votes : {}'.format(self.name,self.position,self.votes)

    class Meta:
        verbose_name_plural = "Candidate List"

                                                                                                            # On / Off
#[+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++]
#Creating the on off swith to control the vote..
class sms(models.Model):
    switch_choices = (
        ('ON','Turn ON the VOTING/BALLOT'),
        ('OFF','Turn OFF the VOTING/BALLOT'),
    )
    switch = models.CharField(max_length=3, choices=switch_choices)
    messaging = models.TextField(max_length=80,blank=True) 

    def __str__(self):
        return 'EDIT (here only) : Voting Status : {}  | Message Displaying :{}'.format(self.switch,self.messaging)
    
    class Meta:
        verbose_name_plural = "Voting Status Control"