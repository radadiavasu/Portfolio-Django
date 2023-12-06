from django.shortcuts import render
from content.forms import ContactForm
from content.models import *

# for sending email & contact
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.template import loader
from django.contrib import messages

# Create your views here.
def Homepage(request):
    profile = Profile.objects.first()
    about = About.objects.first()
    primary_skill = PrimarySkill.objects.all()
    secondary_skill = SecondarySkill.objects.all()
    services = Service.objects.all()
    projects = MyProject.objects.all()
    portfolios = Portfolio.objects.all()
    testomonial = Testomonial.objects.all()
    form = ContactForm()
    context = {
        'profile':profile,
        'about':about,
        'skill1':primary_skill,
        'skill2':secondary_skill,
        'services':services,
        'projects': projects,
        'portfolios': portfolios,
        'testo':testomonial,
        'form':form,
    }
    return render(request, "index.html",context)

def MailContact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            data = Contact()
            data.fullname = form.cleaned_data['fullname']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.phone_number = form.cleaned_data['phone_number']
            data.message = form.cleaned_data['message']
            data.save()
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            fullname = form.cleaned_data['fullname']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ['vasuradadia850@gmail.com',]
            html_message = loader.render_to_string(
                'email.html',
                {
                    'subject':subject,
                    'message':message,
                    'fullname':fullname,
                    'email':email,
                    'phone_number':phone_number,
                }
            )
            if subject and message and email_from and recipient_list and html_message:
                try:
                    send_mail(subject, message, email_from, recipient_list, html_message = html_message, fail_silently=False)
                except:
                    messages.error(request,"Cannot send mail right now, Try again later")
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                messages.success(request,"Message sent successfully")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                messages.error(request,"Please! Make sure all fields are entered and valid.")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request,"Please! Make sure all fields are entered and valid.")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 