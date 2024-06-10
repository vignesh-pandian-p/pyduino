from django.shortcuts import render,redirect,HttpResponse
import io
import sys,time
import secrets
import string,json
from .models import Register,API,Messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from django.contrib import messages 


# Create your views here.
def index(request):
    return render(request,"main/index.htm")


def news(request):
        return render(request,"main/news.htm")

   

def signup(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        email=request.POST["email"]
        confirm=request.POST["confirm"]
        print(username,password,confirm,email)
        if password==confirm:
            if not Register.objects.filter(username=username).exists():
                data=Register.objects.create(username=username,password=password,email=email)
                data.save()
                return redirect("login")
            else:
                return redirect("signup")

    return render(request,"main/signup.htm")

def login(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        if (Register.objects.filter(username=username).exists()):
            user=Register.objects.get(username=username)
            if password==user.password:
                request.session['username'] = username
                
                return redirect("index")
                
    return render(request,"main/login.htm")
def generate_random_key(length=16):
    alphanumeric_chars = string.ascii_letters + string.digits
    random_key = ''.join(secrets.choice(alphanumeric_chars) for _ in range(length))
    return random_key





from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
def internlogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        domain = request.POST.get('domain')

        try:
            user = User.objects.get(email=email, domain=domain)
            
            if domain == "Web Development":
                return render(request, 'main/webtask.htm')
            elif domain == "AI":
                return render(request, 'main/aitask.htm')
            elif domain == "IoT Development":
                return render(request, 'main/iottask.htm')
            elif domain == "UI-UX Design":
                return render(request, 'main/uiuxtask.htm')
            elif domain == "Mobile Application":
                return render(request, 'main/mobtask.htm')
            
        except User.DoesNotExist:
            messages.error(request, 'Invalid email or domain.')
            return render(request, 'main/intern.htm')  # Redirect to the login page if credentials are invalid

    return render(request, 'main/intern.htm')  # Render the login page if the request method is not POST
def internregister(request):
    return render(request, "main/regester.htm")
def intern(request):
    return render(request, "main/intern.htm")

    # session_value = request.session.get("username", "guest")
    
    # if session_value != "guest":
    #     data = Register.objects.get(username=session_value)
        
    #     if request.method == "POST":
    #         api_value = generate_random_key()
            
    #         if API.objects.filter(user=data).exists():
    #             existing_api = API.objects.get(user=data)
    #             existing_api.apiKey = api_value
    #             existing_api.save()
    #         else:
    #             API.objects.create(user=data, apiKey=api_value)
            
    #         return redirect("api")
        
    #     if API.objects.filter(user=data).exists():
    #         api_value = API.objects.get(user=data)
    #         return render(request, "main/intern.htm", {"apiValue": api_value})
    #     else:
    #         return render(request, "main/intern.htm")
    
    # else:
    #     return redirect("/")      
    

def deleteAPI(request,id):
    if API.objects.filter(id=id).exists():
        data=API.objects.get(id=id)
        data.delete()
        return redirect("api")
    else:
        return redirect("home")
    


@csrf_exempt
def communityBE(request):
    print("babay")
    if request.method == 'POST':
        message = request.POST.get('message', '')
        username = request.session.get("username", "guest")
        data = Messages.objects.create(message=message, username=username)
        data.save()
        print("baby")

        response_data = {'status': 'success', 'message': message, 'username': username}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

    
def  community(request):
    data=Messages.objects.all()
    return render(request,"main/community.htm",{"data":data})

def get_messages(request):
    messages = list(Messages.objects.values())
    return JsonResponse(messages, safe=False)


from django.shortcuts import render, redirect
from .models import InternshipApplication
from .forms import InternshipApplicationForm

def internship_application(request):
    if request.method == 'POST':
        form = InternshipApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # This saves the form data to the InternshipApplication model
            return render(request,"main/success.htm")  # Redirect to a success page or another URL
    else:
        form = InternshipApplicationForm()
    
    return render(request, 'regester.html', {'form': form})



def sendMail(request):
    fullname=request.POST["fullname"]
    email=request.POST["email"]
    message=request.POST["message"]
    print(fullname,email,message)   
    sender_email = "mjanokodesh@gmail.com"
    receiver_email = "mjanokodesh@gmail.com"
    subject = "Support Request TECKO"
    body = f"User Detail and Request \nFull Name - {fullname}\nE-Mail - {email}\nMessage - {message}"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))

    smtp_server = "smtp.gmail.com" 
    smtp_port = 587  
    smtp_username = "mjanokodesh@gmail.com"  
    smtp_password = "tjqz mnsw fsrp ykcc"

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  
            server.login(smtp_username, smtp_password)
            server.sendmail(sender_email, receiver_email, message.as_string())

    except Exception as e:
        print(f"Error sending email: {e}")
    return render(request,"main/email.htm")
    
def tools(request):
    return render(request,"main/tools.htm")



def contact(request):
    return render(request,"main/contact.htm")

def otp(request):
    return render(request,"main/otp.htm")

def demo(request):
    return render(request,"main/demo.htm")

@csrf_exempt
def apiCall(request):
    output_buffer = io.StringIO()
    original_stdout = sys.stdout
    data = {}
    if request.method == 'POST':
        print("successfully done request from arduino")
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            apiKey = data.get('apiKey')
            pythonCode = data.get('pythonCode')
            
            if Register.objects.filter(username=username).exists():
                dataValue = Register.objects.get(username=username)
                Id = dataValue.id
                pword = dataValue.password
                ApiValue = API.objects.get(user=Id)
                ApiKey = ApiValue.apiKey 
                if apiKey == ApiKey and pword == password:
                    try:
                        sys.stdout = output_buffer
                        startTime = time.time()
                        exec(pythonCode)
                        endTime = time.time()
                        executionTime = endTime - startTime
                    except Exception as e:
                        print(e)
                        errorList = []
                        errorList.append(e)
                        return JsonResponse({'error': str(e)})
                    finally:
                        sys.stdout = original_stdout
                        captured_output = output_buffer.getvalue()
                        output = captured_output.splitlines()
                        data['output'] = output
                        data['executionTime'] = executionTime
                        return JsonResponse(data)
        except Exception as e:
            print("Error:", e)
            return JsonResponse({'error': str(e)})
    
    return JsonResponse(data)