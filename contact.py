EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com.'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'your email'
EMAIL_HOST_PASSWORD = 'your email password'

class AdminContactForm(forms.ModelForm):
    fullname = forms.CharField(required=True,max_length=100)
    email = forms.EmailField(required=True,max_length=100)
    subject = forms.CharField(required=True,max_length=300)
    phone = forms.CharField(required=True,max_length=100)
    message = forms.CharField(required=True,widget=forms.Textarea)

    class Meta:
        model = AdminContact
        fields = [
            'fullname',
            'email',
            'subject',
            'message',
            'phone',
        ]

    def __init__(self, *args, **kwargs):
        super(AdminContactForm, self).__init__(*args, **kwargs)
        self.fields['fullname'].widget.attrs['placeholder'] = 'Full Name'
        self.fields['email'].widget.attrs['placeholder'] = 'E-mail Address'
        self.fields['subject'].widget.attrs['placeholder'] = 'Subject'
        self.fields['phone'].widget.attrs['placeholder'] = 'Contact Number'
        self.fields['message'].widget.attrs['placeholder'] = 'Message'
        self.fields['fullname'].widget.attrs['class'] = 'name half'
        self.fields['phone'].widget.attrs['class'] = 'phone half ml-3'
        self.fields['email'].widget.attrs['class'] = 'email'
        self.fields['subject'].widget.attrs['class'] = 'web'
    
    
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.template import loader

def admincontact(request):
    if request.method == "POST":
        form = AdminContactForm(request.POST)
        if form.is_valid():
            data = AdminContact()
            data.fullname = form.cleaned_data['fullname']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.phone = form.cleaned_data['phone']
            data.message = form.cleaned_data['message']
            data.save()
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            fullname = form.cleaned_data['fullname']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ['your email',]
            html_message = loader.render_to_string(
                'email.html',
                {
                    'subject':subject,
                    'message':message,
                    'fullname':fullname,
                    'email':email,
                    'phone':phone,
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
        


from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.INFO: 'primary',
    messages.SUCCESS: 'success',
    messages.WARNING: 'danger',
    messages.ERROR: 'danger',
    50: 'critical',
}

{% if messages %}
{% for message in messages %}
<div id="index-alert"
    class="alert {% if message.tags %}alert-{{ message.tags }}{% endif %} alert-dismissible bg-{% if message.tags == 'success' %}success{% elif message.tags == 'danger' %}danger{% elif message.tags == 'primary' %}primary{% endif %}">
    <a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a>
    <strong class="text-white"> {% if message.tags == 'success' %}Success{% elif message.tags == 'danger' %} Error {% elif message.tags == 'primary' %}Message{% endif %} ! </strong><span class="text-white">{{message}}</span>
</div>
{% endfor %}
{% endif %}

<script>
  window.setTimeout(function () {
      $("#index-alert").fadeTo(800, 0).slideUp(800, function () {
          $(this).remove();
      });
  }, 2000);
</script>