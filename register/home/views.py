from http.client import SWITCHING_PROTOCOLS
from platform import release
from django.forms import ValidationError
from django.shortcuts import redirect, render,HttpResponse
from home.models import Contact,Student_Registration,Candidate,Positions,Logged,sms
from datetime import datetime
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


# Create your views here.
def index(request):
    return render(request, 'index.html')


#[-------------------------------this is the user registration area...---------------------------------------------------------------]
def register(request):
    if request.method == "POST" :
        # Reading the data from the post requst..
        firstName = request.POST.get('firstName')
        middleName = request.POST.get('middleName')
        lastName = request.POST.get('lastName')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        rollNumber = request.POST.get('rollNumber')
        department = request.POST.get('department')
        year = request.POST.get('year')

        #checking the year for empty string...
        conv = lambda i : i or ''
        res = conv(year)
        #check the department for empty string..
        conv = lambda i : i or ''
        dept = conv(department)




        # $$$$$===============   checking the user inputs..on the registration form.. ==========$$$
        if (firstName == "" or lastName == "" or telephone == "" or email == "" or rollNumber == "" or dept == "" or res == ""):
            #print(year)
            #if (year!=year.int()):
                #print(1 + ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                #messages.warning(request, 'Ooops ! Unable to submit form due to empty fields.')
                #return redirect('register')
                #messages.warning(request, 'Ooops ! Unable to submit form due to empty fields.')
                #return redirect('register')
            #else:
                #print(0)
                #messages.warning(request, 'Ooops ! Unable to submit form due to empty fields.')
                #return redirect('register')
                messages.warning(request, 'Ooops ! Unable to submit form due to empty fields.')
                return redirect('register')

        else:
            if Student_Registration.objects.filter(email=email).exists():
                messages.warning(request, '***You have already registered an account with this information ! Go to Login now.')
                return redirect('register')

        #creating the objects ..<student_registraiton>....
            else:
                #####################################################################################_
                # @@@@@@@@@@@@@@@@@@@@@@@@@@@      Email validation !!      @@@@@@@@@@@@@@@@@@@@@@@@@
                ####################################################################################
                # try:
                #      validate_email(value)
                # except ValidationError as e:
                #      print("bad email, details:", e)
                # else:
                #      print("good email")

                try:
                    validate_email(email)
                except ValidationError as e:
                    messages.warning(request, "*Bad email, details :" + str(e))
                    return redirect('register')
                else:
                    register_person = Student_Registration(
                        firstName=firstName, middleName=middleName, lastName=lastName, 
                        email=email,
                        telephone=telephone,
                        rollNumber=rollNumber,
                        department=department,
                        year=year
                        )
                    #our object here is the "register_person"...
                    register_person.save()
                    messages.success(request, 'Your account has been registered !\n Your login password is your mobile number.',extra_tags='green-text' )
                    
                    return redirect('register')
                    #creating the global function here .....
                    #[+++++++++++++++++++++++]----login validation----[++++++++++++++++++++++++++]
                    #Function starts here....
                    #MyObject.objects.filter(someField=someValue).exists() # return True/False

    data = sms.objects.all()    
    return render(request, 'register.html',{'data':data})
    #end of the registration form area and the final request..

    #created a global function to be accessed by the login paramters to check the presence of data in the database..

#[----------------------------LOGIN request handling area..--------------------------------------------------------------------------]
def login(request):
    
    
    def checking_input_parameters(username, password):
        if Student_Registration.objects.filter(email=username).exists():
            if Student_Registration.objects.filter(telephone=password).exists():
                return 1
            else:
                return 0
        else:
            return 2

    if request.method == "POST" :

        username = request.POST.get('email')
        password = request.POST.get('password')


        #checking the user inputs for validation with the backend.....
        if( username != "" and password != "" ):
            #looking the entries in the database....
            #call the global function from the register function..
            yohoo = checking_input_parameters(username, password)
            print(yohoo)
            if yohoo == 1:
                # cheicking if the voting is active..
                ##################################################
                if sms.objects.filter(switch='ON').exists():
                    messages.success(request, 'You have logged in successfully.', extra_tags='green-text text-darken-4')
                    return redirect('SGlkZGVuIExvZ2luIFBhbmVs')
                else:
                    messages.warning(request, '*No voting is available current now')
                    return redirect('login')

                #################################################
                
            elif yohoo == 0:
                messages.warning(request, '*Ooops ! Unable to login due to incorrect password.')
                return redirect('login')
            else:
                messages.warning(request, '*You have entered a wrong email !')
                return redirect('login')
        else:
            messages.warning(request, '*Sorry, Empty feilds are not acceptable !')
            return redirect('login')
                

    show = sms.objects.all()
    return render(request, 'login.html',{'show':show})



#[---------------------------Voting page for the ballot----------------------------------------------------------------------------------]

def vote(request):
    return render(request, 'vote.html')   

def about(request):
    return render(request, 'about.html')

def developer(request):
    return render(request, 'developer.html')

def success(request):
    return render(request, 'sms.html')


#[------------this is the method to bring the contact information from the contact.html page.-------------------------------------------]

def contact(request):
    if request.method == "POST":
        email = request.POST.get('email')
        message = request.POST.get('message')
        phone = request.POST.get('phone')
        #checking user inputs..
        if (email == "" or message == "" or phone == "" ):
            messages.warning(request, 'Ooops ! Unable to submit form due to empty fields.')
            return redirect('contact')
        else:
        #creating the object..<contact>..
            contact = Contact(email=email, phone=phone, message=message, date=datetime.today())
            contact.save()
            messages.success(request, 'Thanks! We appreciate that you\'ve taken the time to write us. We\'ll get back to you very soon.')
            return redirect('contact')
    
    return render(request, 'contact.html')

#[---------------------------hidden panel for logged usrs voter panel------------------------------------------------------------------]

def SGlkZGVuIExvZ2luIFBhbmVs(request):
    def is_present(userEmail):
        if Student_Registration.objects.filter(email=userEmail).exists():
            # Then check if it also exits in the volted students table..
            if Logged.objects.filter(email=userEmail).exists():
                # if it is present in the list of Voted students ie models.Logged 
                # then return error message "You have already voted..."
                return 0
                # return zero means that the usr has alredy voted
            else:
                # got the email to the object...already..
                # now creating the instance...of the retrieved object 
                # and linking it to the database with the model.Logged(email=userEmail)
                #email_instance = Logged(email=userEmail)
                # save this instance...
                #email_instance.save()
                return 1
                # return 1 suggests that user has not voted yet...

        else:
            return 2
            # return 2 => that the userEmail is not found in the database..ie he is not registered..
            



    #_Getting the requst as POST from the form...
    if request.method == "POST" :
        userEmail = request.POST.get('email')

        #check the input string for the userEmail..
        if( userEmail != ''):
            check = is_present(userEmail)
            if(check == 0):
                messages.warning(request, 'Looks like you have already voted once !!!' )
                return redirect(login)
            
            elif(check == 1):              
                for position in Positions.objects.only('name'):
                                                              # it will check for the position in the Positions table..
                    choices = request.POST.get(str(position))
                                                              # this will get the id of the selected person from the request..
                    if Candidate.objects.filter(pk=choices).exists():
                        instance = Candidate.objects.get(pk=choices)
                                                              # this statement will create an instance to the primary key related to the candidate
                        instance.votes += 1
                                                               # this statement will add a vote the instance linking to that particular name...
                        instance.save()
                        # this will finally save the vote to the database for the respected field..
                    else:
                        continue
                stu_data = Student_Registration.objects.get(email=userEmail)
                print(stu_data)
                voter_email = Logged(email=userEmail,details=stu_data)
                voter_email.save()
                return redirect('success')

            else:
                messages.warning(request, 'Unable to find your email in the Database !!!')
                return redirect(login)    
        else:
            messages.warning(request, '*You have not entered you email. Please try to submit again with your e-mail.')
            return redirect('SGlkZGVuIExvZ2luIFBhbmVs')


    #_rendering this data as template....to the html from the models models.Candidate and models.Position..
    candidates = Candidate.objects.all()
    position = Positions.objects.all().order_by('priority')
    return render(request, 'SGlkZGVuIExvZ2luIFBhbmVs.html',{'candidates': candidates,'positions':position})


## ++++++++++++++++++++++++++++++++++++++++++++++++++++++++

###$$$$$$$$     Fetching Errors :::::

def error_404(request,exception):
        data = {}
        return render(request,'404.html', data)

def error_500(request):
        data = {}
        return render(request, '500.html', data)