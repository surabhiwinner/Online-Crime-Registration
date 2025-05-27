from django.core.mail import EmailMultiAlternatives

from django.template.loader import render_to_string


from django.conf import settings



def send_email(subject, recepient,template,context):

    mail = EmailMultiAlternatives(subject=subject,from_email=settings.EMAIL_HOST_USER, to=[recepient])

    content = render_to_string(template,context)

    mail.attach_alternative(content,'text/html')

    mail.send()