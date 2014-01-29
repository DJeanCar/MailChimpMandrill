from django.shortcuts import render, redirect
from django.core.mail import EmailMessage


def home(request):
	return render(request, 'index.html')

def send_email(request):
	msg = EmailMessage(subject="Bienvenido", from_email="MJeanC.104@gmail.com",
                   to=["jean_carlos104@hotmail.com"])
	msg.template_name = "Bienvenida"
	msg.template_content = {                  
    			"cambio" :  "<h1>HOLAAAAAAAAAAAA</h1>"
			}

	msg.send()
	return redirect('/')